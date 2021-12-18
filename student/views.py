from mainsias_dj.easy import *
from django.db.models import Q
from auth_api.serializers import UserSerializer, GetUserSerializer, UserShortSerializer
from student.serializers import StudentSubscriptionRecordSerializer, StudentSubscriptionsQuestionsRecordSerializer,\
    GetStudentSubscriptionRecordSerializer, GetStudentSubscriptionRecordFullSerializer
from student.models import StudentSubscriptionRecord, StudentSubscriptionsQuestionsRecord
from subscription.models import Subscription, SubscriptionQuestionAllowence, SubscriptionPaymentDetails
from subscription.serializers import GetSubscriptionSerializer
from evaluation.models import Evaluation
from evaluation.serializers import GetFullEvaluationSerializer
from exam.models import Exam
from exam.serializers import ExamShortSerializer

def addRegistrationFreeBenifits(sid):

    exam = Exam.objects.get(short_name="SUBMITFORFREE")
    free_subscription = Subscription.objects.filter(exam=exam, active=True)
    for i in free_subscription:
        this_expiry = timeAfter(i.days-1).date() if i.days else i.till_date
        free_subscription_i = StudentSubscriptionRecordSerializer(data={
            "student" : sid,
            "exam" : exam.id,
            "subscription_name" : i.name,
            "paid" : i.price,
            "selling_points" : i.selling_points,
            "expiry_date" : this_expiry,
        })
        if not free_subscription_i.is_valid(): 
            return Response({"result":'error'})
        free_subscription_i = free_subscription_i.save()
        free_allowences = GetSubscriptionSerializer(i).data['subscription_allowences']
        for j in free_allowences:
            StudentSubscriptionsQuestionsRecord(subscription=free_subscription_i,subject_name=j['subject_name'],\
            question_number=j['question_number'],frequency=j['frequency'],category_id=j['category']).save()


class AddSubscriptionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            if isStudent(request.user):
                if self.kwargs['do'] == "subscription":
                    payments = SubscriptionPaymentDetails.objects.get(order_id=request.data['order_id'])
                    payments.signature = request.data['signature']
                    payments.payment_id = request.data['payment_id']
                    payments.is_paid = True
                    subscription = Subscription.objects.get(id=request.data['subscription']['id'])
                    subscription_allowences = SubscriptionQuestionAllowence.objects.filter(subscription=subscription)
                    if subscription.days:
                        expiry_date = timeAfter(subscription.days-1).date()
                    else: expiry_date = subscription.till_date 
                    add_subscription = StudentSubscriptionRecordSerializer(data={
                        "student" : request.user.id,
                        "exam" : subscription.exam.id,
                        "subscription_name" : subscription.name,
                        "paid" : subscription.price,
                        "selling_points" : subscription.selling_points,
                        "purchase_time" : timezone.localtime(),
                        "expiry_date" : expiry_date,
                    })
                    if add_subscription.is_valid(): 
                        add_subscription = add_subscription.save()
                        payments.subscription_subscribed=add_subscription
                        payments.save()
                    for i in subscription_allowences:
                        StudentSubscriptionsQuestionsRecord(subscription=add_subscription, subject_name=i.subject_name, question_number=i.question_number, category=i.category, frequency=i.frequency).save()
                    return Response({'result':True, "new_subscription":GetStudentSubscriptionRecordSerializer(add_subscription).data})
            return Response({'result':False})
        except KeyboardInterrupt:
            return Response({'result':'error'})

class DoStudentsView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            context = {'result' : True, 'students_list':[]}
            if self.kwargs['do'] == "search" and isAdmin(request.user):
                if not request.query_params['q'] == "":
                    context['students_list'] = UserShortSerializer(User.objects.filter(isStudent=True).filter(Q(email__icontains=request.query_params['q'])\
                        |Q(first_name__icontains=request.query_params['q'])|Q(last_name__icontains=request.query_params['q'])), many=True).data
                if len(context['students_list']) == 0:
                    context['result'] = "not_found"
                return Response(context)

        except KeyboardInterrupt:return Response({'result':'error'})
        return Response({'result':False})
    
class DoStudentView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do'] == "a-subscribed-subscription-detail":
                subscribed_subscription = GetStudentSubscriptionRecordFullSerializer(\
                    StudentSubscriptionRecord.objects.get(id=request.data['ssid'])).data
                context['individual_subscribed_subscription_detail'] = subscribed_subscription

            return Response(context)

        except KeyboardInterrupt:
            return Response({'result':'error'})
        return Response({'result':False})

    def get(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            
            if self.kwargs['do'] == "get-full-details":
                context["profile"] = GetUserSerializer(User.objects.get(id=self.kwargs['student_id'])).data
                context["subscriptions"] = GetStudentSubscriptionRecordFullSerializer(\
                    StudentSubscriptionRecord.objects.filter(student_id=self.kwargs['student_id']), many=True).data
                context['evaluations'] = GetFullEvaluationSerializer(Evaluation.objects.filter(\
                    student_id=self.kwargs['student_id']), many=True).data

            return Response(context)

        except KeyboardInterrupt:
            return Response({'result':'error'})
        return Response({'result':False})
    

class DoStudentExamView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            if isStudent(request.user):
                context = {'result':True}
                if self.kwargs['exam_short_name'] == 'all':
                    if self.kwargs['do'] == "get-subscribed":
                        subscribed_record_obj = StudentSubscriptionRecord.objects.filter(student=request.user)
                        if request.query_params.get('where') == "home": 
                            if len(subscribed_record_obj)>4: subscribed_record_obj = subscribed_record_obj[0:4]
                        context['subscribed_record'] = GetStudentSubscriptionRecordFullSerializer(subscribed_record_obj, many=True).data
                else:
                    exam_obj = Exam.objects.get(short_name=self.kwargs['exam_short_name'])
                    context["exam"] = ExamShortSerializer(exam_obj).data
                    # if self.kwargs['do'] == "get-all":
                    #     subscriptions_obj = Subscription.objects.filter(exam_id=exam_obj.id)
                    #     context["subscriptions"] = GetSubscriptionSerializer(subscriptions_obj, many=True).data
                    if self.kwargs['do'] == "get-subscribed":
                        subscribed_record_obj = StudentSubscriptionRecord.objects.filter(exam=exam_obj, student=request.user)
                        context['subscribed_record'] = GetStudentSubscriptionRecordSerializer(subscribed_record_obj, many=True).data
                return Response(context)

            return Response({'result':False})
        except KeyboardInterrupt:
            return Response({'result':'error'})

    def post(self, request, *args, **kwargs):
        if isTopToStudentLevel(request.user):

            return Response({'result':True})
        return Response({'result':False})
