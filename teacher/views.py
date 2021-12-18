from mainsias_dj.easy import *
from auth_api.serializers import UserSerializer, GetUserSerializer, UserShortSerializer
from django.contrib.auth.hashers import make_password
from .models import EvaluatorPaymentDetails, EvaluatorGlance, GlanceEvaluationsRecord, EvaluatorRating, EvaluatorCategoryPricing
from .serializers import GetEvaluatorPaymentDetailsSerializer, GetEvaluatorGlanceSerializer, GetPreviousEvaluatorGlanceSerializer, GetEvaluatorRatingSerializer
from subscription.models import SubscriptionQuestionCategory
from evaluation.models import Evaluation
from django.db.models import Sum

class CreateTeacherView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if isTopToManagerLevel(request.user):
            try:
                if User.objects.filter(email=request.data['email']): return Response({'result':'emailExist'})
                teacher_serializer = UserSerializer(data=request.data)
                if teacher_serializer.is_valid():
                    teacher = teacher_serializer.save(created_by=request.user,password=make_password\
                    (request.data['password']), isTeacher=True, isVerified=True)
                    EvaluatorPaymentDetails(evaluator=teacher).save()
                    EvaluatorGlance(evaluator=teacher).save()
                    EvaluatorRating(evaluator=teacher).save()
                    return Response({'result':True})
            except :
                return Response({'result':'error'})
        return Response({'result':False})

class DoTeacherView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs.get('do') == "details":
                context["teacher_details"] = GetUserSerializer(User.objects.get(id=self.kwargs['tid'],isTeacher=True)).data
            elif self.kwargs.get('do') == "get-payment-details":
                context["payment_details"] = GetEvaluatorPaymentDetailsSerializer(\
                EvaluatorPaymentDetails.objects.get(evaluator_id=self.kwargs['tid'])).data
                
            elif self.kwargs.get('do') == "get-summary":

                evaluator = User.objects.get(id=self.kwargs['tid'],isTeacher=True)
                context['evaluator_rating'] = GetEvaluatorRatingSerializer(EvaluatorRating.objects.get(evaluator=evaluator)).data
                context['glance_all_details'] = []
                all_available_categories = SubscriptionQuestionCategory.objects.all()
                eval_evaluations = Evaluation.objects.filter(evaluator=evaluator)
                for i in all_available_categories:
                    tmp_1 = eval_evaluations.filter(category=i).aggregate(Sum('answers_count'))['answers_count__sum']
                    if tmp_1 == 0 or tmp_1 == None: continue
                    context['glance_all_details'].append({
                        "category" : i.name,
                        'count': tmp_1
                    })
                
            elif self.kwargs.get('do') == "get-glance":
                evaluator = User.objects.get(id=self.kwargs['tid'],isTeacher=True)
                context['evaluator_glance'] = GetEvaluatorGlanceSerializer(EvaluatorGlance.objects\
                .get(evaluator=evaluator, status="Current")).data

                
                context['glance_current_details'] = []
                available_categories = SubscriptionQuestionCategory.objects.all()
                for i in available_categories:
                    tmp_ = GlanceEvaluationsRecord.objects.filter(category=i,glance_id=context['evaluator_glance']['id'])
                    tmp_count = 0
                    for j in tmp_:
                        tmp_count += j.evaluation.answers_count
                    if tmp_count == 0: continue
                    tmp_cost = EvaluatorCategoryPricing.objects.filter(evaluator=evaluator,category=i)
                    if tmp_cost:
                        tmp_cost = tmp_cost[0].cost
                    else: tmp_cost = i.evaluation_cost

                    context['glance_current_details'].append({
                        "category" : i.name,
                        "cost" : tmp_cost,
                        'count': tmp_count
                    })
                    
            elif self.kwargs.get('do') == "get-previous-glance":
                evaluator = User.objects.get(id=self.kwargs['tid'],isTeacher=True)
                context['closed_glances'] = GetPreviousEvaluatorGlanceSerializer(EvaluatorGlance.objects\
                .filter(evaluator=evaluator, status="Closed"), many=True).data
            
            return Response(context)

        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs.get('do') == "close-glance":
                evaluator = User.objects.get(id=self.kwargs['tid'],isTeacher=True)
                evaluator_glance = EvaluatorGlance.objects.get(id=request.data['egid'])
                evaluator_glance.closed_details = request.data['closed_details']
                evaluator_glance.status = "Closed"
                evaluator_glance.closed_at = timeNow()
                evaluator_glance.save()
                EvaluatorGlance(evaluator=evaluator).save()
                context['new_closed_glances'] = GetPreviousEvaluatorGlanceSerializer(evaluator_glance).data
            
            return Response(context)

        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})
        

class DoTeachersView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do']=="update-payment-details":
                payment_details = EvaluatorPaymentDetails.objects.get(evaluator=request.user)
                payment_details.details = request.data['payment_details']
                payment_details.save()
                return Response(context)
        except: return Response({'result':'error'})
        return Response({'result':False})
    
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('do') == "get-list":
            teacher_list = UserShortSerializer(User.objects.filter(isTeacher=True),many=True).data
            for i in  range(len(teacher_list)):
                teacher_list[i]['evaluator_ratings'] = GetEvaluatorRatingSerializer(EvaluatorRating.objects.get(evaluator_id=teacher_list[i]['id'])).data
        return Response({'result':True,"teacher_list":teacher_list})
        












        