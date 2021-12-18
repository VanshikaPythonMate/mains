from mainsias_dj.easy import *
from auth_api.serializers import GetUserSerializer, UserShortSerializer
from subscription.serializers import SubscriptionSerializer, GetSubscriptionSerializer, GetSubscriptionFullSerializer,\
    SubscriptionQuestionAllowenceSerializer, GetSubscriptionQuestionCategorySerializer, GetFullManagerEditsSerializer, GetSubscriptionFullSerializerwithExam
from subscription.models import Subscription, SubscriptionQuestionAllowence, SubscriptionQuestionCategory, ManagerEdits,\
    SubscriptionPaymentDetails
from student.serializers import StudentSubscriptionRecord
from evaluation.models import Evaluation
from student.serializers import GetStudentSubscriptionRecordFullSerializer
from django.db.models import Sum
from exam.models import Exam
from exam.serializers import GetExamSerializer, ExamShortSerializer
from .utils import updateSubscription, createSubscription
from mainsias_dj import settings
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY_ID, settings.RAZORPAY_API_KEY_SECRET))

class CreateSubscriptionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if isManager(request.user) and request.user.can_create_subscription:
                
                tmp = {"subscription" : request.data['subscription'],
                        "question_number_allowence":request.data['question_number_allowence']}

                tmp_bkp = json_to_str({"subscription" : request.data['subscription'],
                        "question_number_allowence":request.data['question_number_allowence']})

                tmp['subscription']['exam'] = ExamShortSerializer(Exam.objects.get(id=tmp['subscription']['exam'])).data
                
                for i in tmp['question_number_allowence']:
                    i['category'] = GetSubscriptionQuestionCategorySerializer(\
                        SubscriptionQuestionCategory.objects.get(id=i['category'])).data
                
                ManagerEdits(content_bkp=tmp_bkp, content=json_to_str(tmp),\
                created_by=request.user, note=request.data['note']).save()

            elif isAdmin(request.user):
                if not request.user.id == request.data['subscription']['created_by']: return Response({'result':'invalidUserId'}) 
                context = createSubscription({
                    "subscription": request.data['subscription'],
                    "question_number_allowence":request.data['question_number_allowence']
                })

            return Response(context)
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

class DoSubscriptionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if isTopToManagerLevel(request.user):

                if self.kwargs.get('do') == 'update-active':
                    subscription_obj = Subscription.objects.get(id=request.data['sid'])
                    if isAdmin(request.user):
                        subscription_obj.active = request.data['active']
                        subscription_obj.save()
                    else:
                        tmp_raw = GetSubscriptionFullSerializerwithExam(subscription_obj).data
                        tmp = {'subscription':tmp_raw,'active':request.data['active'],
                            'question_number_allowence':tmp_raw['subscription_allowences'],'sid':request.data['sid']}
                        del tmp['subscription']['subscription_allowences']
                        ManagerEdits(_type=f"Active-toggle", content=json_to_str(tmp),\
                        created_by=request.user, note=f"Active button toggled to {request.data['active']}").save()                   
                    
                    context['active'] = request.data['active']
                
                elif self.kwargs.get('do') == 'update-featured':
                    subscription_obj = Subscription.objects.get(id=request.data['sid'])
                    if isAdmin(request.user):
                        subscription_obj.featured = request.data['featured']
                        subscription_obj.save()
                    else:
                        tmp_raw = GetSubscriptionFullSerializerwithExam(subscription_obj).data
                        tmp = {'subscription':tmp_raw,'featured':request.data['featured'],
                            'question_number_allowence':tmp_raw['subscription_allowences'],'sid':request.data['sid']}
                        del tmp['subscription']['subscription_allowences']
                        ManagerEdits(_type=f"Featured-toggle", content=json_to_str(tmp),\
                        created_by=request.user, note=f"Featured button toggled to {request.data['featured']}").save()                   
                    
                    context['featured'] = request.data['featured']
            
            return Response(context)
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

    def get(self, request, *args, **kwargs):
        try:
            if self.kwargs.get('do') == 'get-subjects-category-list':
                return Response({
                    'result':True,
                    "category_list":GetSubscriptionQuestionCategorySerializer(SubscriptionQuestionCategory.objects.all(), many=True).data
                    })

            elif self.kwargs.get('do') == 'manager-updates' and isAdmin(request.user):
                return Response({
                    'result':True,
                    "requests":GetFullManagerEditsSerializer(ManagerEdits.objects.all(), many=True).data
                    })

            elif self.kwargs.get('do') == 'get-student-subscribed-allowence-capacity':
                subscribed_subscription_obj = StudentSubscriptionRecord.objects.get(id=request.query_params['ssid'])
                subscribed_subscription = GetStudentSubscriptionRecordFullSerializer(subscribed_subscription_obj).data
                current_capacity = []
                date_differnce_from_purchase = dateDiff(timezone.localdate(), subscribed_subscription_obj.purchase_time.date())
                for i in subscribed_subscription['student_subscribed_allowences']:
                    if i['frequency'] <= 0:
                        answers_count = Evaluation.objects.filter(subject_id=i['id'], student=request.user).\
                        aggregate(Sum('answers_count'))['answers_count__sum']
                    else:
                        from_date = calculate_from_date(date_differnce_from_purchase ,i['frequency'])
                        answers_count = Evaluation.objects.filter(subject_id=i['id'], date__gte=from_date, student=request.user).\
                        aggregate(Sum('answers_count'))['answers_count__sum']
                    if answers_count == None: answers_count=0
                    if answers_count < i['question_number']:
                        current_capacity.append({"id": i['id'],"subject_name": i['subject_name'],"question_number": i['question_number']-answers_count})
                    elif answers_count > i['question_number']:
                        return Response({'result':'wrong_method',"detail":"submitted more than allowed, subscription can be rejected"})
                return Response({'result':True,"updated_allowences":current_capacity,"from_date":from_date})

        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

        
class SubscriptionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Response({})

    def get(self, request, *args, **kwargs):
        try:
            context = {'result':True}

            if self.kwargs.get('do') == 'get-list':
                context['subscription_list'] = []
                subscription_obj = Subscription.objects.filter(exam_id=self.kwargs.get('eid'), active=True)
                for i in subscription_obj:
                    context['subscription_list'].append({'subscription' : GetSubscriptionFullSerializer(i).data})
            
            elif self.kwargs.get('do') == 'sub-details':
                subscription_obj = Subscription.objects.get(id=self.kwargs.get('eid'))
                context['subscription_details'] = GetSubscriptionFullSerializer(subscription_obj).data
            
            elif self.kwargs['do']=="buy-now":

                subscription = Subscription.objects.get(id=self.kwargs.get('eid'))
                
                receipt_id = timeNow().strftime("receipt_%Y%m%d%H%M%S-PaymentInit")

                send_data = {
                    "amount" : subscription.price*100,
                    "currency" : 'INR',
                    "receipt" : receipt_id,
                    "payment_capture" : "1",
                }

                razorpay_order = client.order.create(data=send_data)

                SubscriptionPaymentDetails(subscription=subscription,student=request.user,order_id=razorpay_order['id'],\
                    order_obj=json_to_str(razorpay_order),receipt_id=receipt_id).save()
                
                context['order_id'] = razorpay_order['id']
                
            return Response(context)

        except KeyboardInterrupt: Response({'result':'error'})
        return Response({'result':False})

    def delete(self, request, *args, **kwargs):
        try:
            context = {'result':True}

            if self.kwargs.get('do') == 'delete':
                if Subscription.objects.filter(id=self.kwargs['eid']).delete(): 
                    context['id'] = self.kwargs.get('eid')
                    return Response(context)
        
        except: return Response({'result':'error'})
        return Response({'result':False})



    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if isTopToManagerLevel(request.user):

                if self.kwargs.get('do') == 'update-subscription':

                    if isAdmin(request.user):

                        context = updateSubscription({
                            'subscription' : request.data['subscription'],
                            "question_number_allowence":request.data['question_number_allowence']
                        }, self.kwargs['eid'])
                        context['subscription'] = GetSubscriptionFullSerializer(context['subscription']).data

                    elif isManager(request.user):

                        tmp = {"subscription" : request.data['subscription'],
                                "question_number_allowence":request.data['question_number_allowence'],"sid":self.kwargs['eid']}

                        tmp_bkp = json_to_str({"subscription" : request.data['subscription'],
                                "question_number_allowence":request.data['question_number_allowence'],"sid":self.kwargs['eid']})

                        tmp['subscription']['exam'] = ExamShortSerializer(Exam.objects.get(id=tmp['subscription']['exam'])).data
                        
                        for i in tmp['question_number_allowence']:
                            i['category'] = GetSubscriptionQuestionCategorySerializer(\
                                SubscriptionQuestionCategory.objects.get(id=i['category'])).data
                        
                        ManagerEdits(_type="Update", content_bkp=tmp_bkp, content=json_to_str(tmp),\
                        created_by=request.user, note=request.data['note']).save()                   
                        
                        context['subscription'] = GetSubscriptionFullSerializer(Subscription.objects.get(id=self.kwargs['eid'])).data
            
            return Response(context)
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})