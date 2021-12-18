from decimal import Context

from django.utils.translation import activate
from mainsias_dj.easy import *
from .serializers import ExamManagerRelationSerializer, ExamShortSerializer, ExamSerializer, GetExamFullSerializer, GetExamSerializer,\
     GetExamListExamManagerRelationSerializer
from .models import ExamManagerRelation, Exam
from subscription.models import Subscription
from subscription.serializers import GetSubscriptionSerializer,GetSubscriptionFullSerializer

class CreateExamView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def post(self, request, *args, **kwargs):
        if isAdmin(request.user):
            exam_serializer = ExamSerializer(data=request.data)
            if exam_serializer.is_valid(): exam_serializer.save(); return Response({'result':True})
        return Response({'result':False})

class DoExamView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request, *args, **kwargs):
        context = {'result':True}
        try:
            if self.kwargs.get('do') == "get-list":
                if isManager(request.user):
                    context['exam_list'] = GetExamListExamManagerRelationSerializer(\
                        ExamManagerRelation.objects.filter(manager=request.user, active=True),many=True).data
                    tmp = []
                    for i in context['exam_list']:
                        tmp.append(i['exam'])
                    context['exam_list'] = tmp
                elif isStudent(request.user) or isAdmin(request.user):
                    context['exam_list'] = ExamShortSerializer(Exam.objects.filter(active=True),many=True).data
                    if request.query_params['assign_to_manager']:
                        context['exam_list'].append(ExamShortSerializer(Exam.objects.get(short_name="SUBMITFORFREE")).data)
                return Response(context)
            elif self.kwargs.get('do') == "get-list-all":
                context['exam_list'] = ExamShortSerializer(Exam.objects.all(),many=True).data      
                return Response(context)
        except: return Response({'result':'error'})
        return Response({'result':False})
    
    def post(self, request, *args, **kwargs):
        pass

class ActionExamView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request, *args, **kwargs):
        try:
            if self.kwargs.get('action') == "details":
                is_offer = True
                if self.kwargs['short_name'] == "SUBMITFORFREE": is_offer = False
                exam = Exam.objects.get(short_name=self.kwargs['short_name'],active=is_offer)
                exam_details = GetExamFullSerializer(exam).data
                if isTopToManagerLevel(request.user):
                    exam_subs = Subscription.objects.filter(exam=exam)
                else:
                    exam_subs = Subscription.objects.filter(exam=exam, active=True)
                exam_details['exam_subscription'] = GetSubscriptionFullSerializer(exam_subs, many=True).data
                return Response({'result':True,"exam_details":exam_details})
            return Response({'result':False})
        except KeyboardInterrupt: return Response({'result':"error"})
    
    def post(self, request, *args, **kwargs):
        try:
            if self.kwargs.get('action') == "update":
                exam_obj = Exam.objects.get(short_name=self.kwargs['short_name'])
                exam_new_details = request.data['exam_details']
                exam_obj.full_name = exam_new_details.get('full_name')
                exam_obj.active = exam_new_details.get('active')
                exam_obj.content1 = exam_new_details.get('content1')
                exam_obj.content2 = exam_new_details.get('content2')
                exam_obj.content3 = exam_new_details.get('content3')
                exam_obj.content4 = exam_new_details.get('content4')
                exam_obj.save()
                return Response({'result':True})
                return Response({'result':True,"exam_details":request.data})

            elif self.kwargs.get('action') == "upload-image":
                exam_obj = Exam.objects.get(short_name=self.kwargs['short_name'])
                exam_obj.image = request.data['image']
                exam_obj.image.name = f"exam-{exam_obj.id}-"+timeNow().strftime("ProfileImage%Y%m%d%H%M%S-Upload")
                exam_obj.save()
                new_image = f"https://evaluations-media-storage.s3.amazonaws.com/media/{str(exam_obj.image)}"
                return Response({'result':True,"image":new_image})
                
            return Response({'result':False})
        except KeyboardInterrupt:return Response({'result':'error'})

    def delete(self, request, *args, **kwargs):
        try:
            if self.kwargs.get('action') == "delete" and isAdmin(request.user):
                if Exam.objects.filter(short_name=self.kwargs['short_name']).delete():
                    return Response({'result':True,"short_name":self.kwargs['short_name']})
        except: return Response({'result':"error"})
        return Response({'result':False})
    

class PublicExamView(APIView):

    def get(self, request, *args, **kwargs):
        if self.kwargs.get('do') == "details":
            if self.kwargs['short_name']=="homepage":
                exam = Exam.objects.get(short_name="SUBMITFORFREE")
                exam_details = GetExamSerializer(exam).data
                featured_subscription = Subscription.objects.filter(exam=exam, featured=True, active=True)
                exam_details['exam_subscription'] = GetSubscriptionSerializer(featured_subscription, many=True).data
                exam_details['image'] = ''
                return Response({ "result":True,"exam_details":exam_details})
                # if need to send differnet data on homepage
                # return Response({ "result":True,"exam_details":{
                #     "short_name":"UPSC",
                #     "full_name":"homepage",
                #     "content1":"Geared up for your Best Prepration",
                #     "content2":"Get your mains preparation assessed and your answers diligently evaluated by UPSC Toppers / Civil Servants / Academic Subject Experts",
                #     "content3":"Some Content",
                #     "content4":"Some content",
                #     "image":"Some content",
                #     "exam_subscription":exam_details['exam_subscription']
                #     }
                # })
            exam = Exam.objects.filter(short_name=self.kwargs['short_name'].upper(),active=True)
            if not exam: return Response({'result':False})
            exam_details = GetExamSerializer(exam[0]).data
            featured_subscription = Subscription.objects.filter(exam=exam[0], featured=True)
            exam_details['exam_subscription'] = GetSubscriptionSerializer(featured_subscription, many=True).data
            return Response({'result':True,"exam_details":exam_details})
        return Response({'result':False})


        
class AllExams(APIView):

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.filter(active=True)
        exam_details = GetExamSerializer(exams, many=True).data
        return Response({'result':True,"exams":exam_details})

