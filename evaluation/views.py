from mainsias_dj.easy import *
from .serializers import EvaluationSerializer,GetFullEvaluationSerializer
from .models import Evaluation
from exam.models import ExamManagerRelation
from teacher.models import EvaluatorGlance, GlanceEvaluationsRecord, EvaluatorRating
from student.models import StudentSubscriptionsQuestionsRecord
from django.db.models import Sum

class AddEvaluationView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            if isStudent(request.user):
                request.data['answer_file'].name = f"EVAL--"+timeNow().strftime("STUDENT-PDF%Y%m%d%H%M%S-FirstUpload")
                
                new_evaluation = Evaluation(
                    student_id=request.data['student'],
                    exam_id=request.data['exam'],
                    subscribed_subscription_id=request.data['subscribed_subscription'],
                    answer_file=request.data['answer_file'],
                    answers_count=request.data['answers_count'],
                    student_message=request.data['student_message'],
                    subject_id=request.data['subject'],
                    category=StudentSubscriptionsQuestionsRecord.objects.get(id=request.data['subject']).category
                    )
                date_differnce_from_purchase = dateDiff(timezone.localdate(), new_evaluation.subscribed_subscription.\
                purchase_time.date())
                if new_evaluation.subject.frequency <= 0:
                    answers_count = Evaluation.objects.filter(subject_id=request.data['subject'],student=request.user,\
                    subscribed_subscription_id=request.data['subscribed_subscription']).aggregate(Sum('answers_count'))['answers_count__sum']
                else:
                    from_date = calculate_from_date(date_differnce_from_purchase, new_evaluation.subject.frequency)
                    answers_count = Evaluation.objects.filter(subject_id=request.data['subject'], date__gte=from_date,student=\
                    request.user,subscribed_subscription_id=request.data['subscribed_subscription']).aggregate(Sum('answers_count'))['answers_count__sum']
                if answers_count == None: answers_count=0
                if answers_count >= new_evaluation.subject.question_number:
                    return Response({'result':False})
                new_evaluation.save()
                GlanceEvaluationsRecord(category=new_evaluation.category,evaluation=new_evaluation).save()
                return Response({'result':True})
            return Response({'result':False})
        except KeyboardInterrupt:
            return Response({'result':'error'})

class DoEvaluationView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do']=="update-evaluator" and isTopToManagerLevel(request.user):
                evaluation = Evaluation.objects.get(id=self.kwargs['evaluation_id'])
                evaluation.evaluator = getUserFromUid(request.data['evaluator_id'])
                evaluation.status = "Assigned"                
                evaluation.save()
                context['evaluation_id'] = evaluation.id
                context['evaluation_status'] = evaluation.status

            elif self.kwargs['do']=="save-evaluator-work" and isTopToTeacherLevel(request.user):
                evaluation = Evaluation.objects.get(id=self.kwargs['evaluation_id'])
                if request.data.get("evaluator_message"): evaluation.evaluator_message = request.data.get("evaluator_message")
                if evaluation.evaluator == request.user or isTopToManagerLevel(request.user):
                    if not evaluation.status == "Evaluated":
                        evaluation.evaluator = request.user
                        evaluation.status = "Evaluated"
                        if not isTopToManagerLevel(request.user):
                            glance_record = GlanceEvaluationsRecord.objects.get(evaluation=evaluation)
                            glance_record.glance = EvaluatorGlance.objects.filter(evaluator=request.user,status="Current")[0]
                            glance_record.save()
                    print(evaluation.evaluated_file)
                    if request.data.get("evaluated_file", False):
                        if not evaluation.evaluator == request.user: return Response({'result':False})
                        evaluation.evaluated_file = request.data["evaluated_file"]
                        evaluation.evaluated_file.name = f"EVAL-{evaluation.id}-"+timeNow().strftime("EVALUATOR-PDF%Y%m%d%H%M%S-Upload")
                    elif not evaluation.evaluated_file:
                        return Response({'result':'File not found'})
                if request.data.get("marks"): evaluation.marks = request.data.get("marks")
                if request.data.get("tags"): evaluation.tags = request.data.get("tags")
                evaluation.save()
                context['evaluation_id'] = evaluation.id
                context['evaluation_status'] = evaluation.status
                context['evaluator_message'] = evaluation.evaluator_message
                context['evaluated_file'] = f"https://evaluations-media-storage.s3.amazonaws.com/media/{str(evaluation.evaluated_file)}"
                context['marks'] = evaluation.marks
                context['tags'] = evaluation.tags

            elif self.kwargs['do']=="save-student-work" and isStudent(request.user):
                evaluation = Evaluation.objects.get(id=self.kwargs['evaluation_id'])
                if request.data.get("student_message"): evaluation.student_message = request.data.get("student_message")
                if request.data.get("answer_file") or not evaluation.answer_file: 
                    evaluation.answer_file = request.data["answer_file"]
                    evaluation.answer_file.name = f"EVAL-{evaluation.id}-"+timeNow().strftime("STUDENT-PDF%Y%m%d%H%M%S-ReUpload")
                if request.data.get("feedback_to_evaluator"): evaluation.feedback_to_evaluator = request.data.get("feedback_to_evaluator")
                if request.data.get("rating_to_evaluator") and not request.data.get("rating_to_evaluator") == '0':
                    if isTeacher(evaluation.evaluator):
                        er_obj = EvaluatorRating.objects.get(evaluator=evaluation.evaluator)
                        if evaluation.rating_to_evaluator == None:
                            er_obj.ratings_total = er_obj.ratings_total + float(request.data.get("rating_to_evaluator"))
                            er_obj.ratings_count += 1
                        else:
                            er_obj.ratings_total = er_obj.ratings_total - evaluation.rating_to_evaluator + float(request.data.get("rating_to_evaluator"))
                        er_obj.save()
                    evaluation.rating_to_evaluator = float(request.data.get("rating_to_evaluator"))
                evaluation.save()
                context['evaluation_id'] = evaluation.id
                context['answer_file'] = f"https://evaluations-media-storage.s3.amazonaws.com/media/{str(evaluation.answer_file)}"

            elif self.kwargs['do']=="reject-answer" and isTopToTeacherLevel(request.user):
                evaluation = Evaluation.objects.get(id=self.kwargs['evaluation_id'])
                evaluation.status = "Rejected"
                evaluation.tags = request.data['tags']
                evaluation.evaluator = request.user
                evaluation.save()
                GlanceEvaluationsRecord.objects.filter(evaluation=evaluation).delete()
                context['tags'] = evaluation.tags
                context['evaluation_id'] = evaluation.id
                context['evaluator_id'] = evaluation.evaluator.id
                context['evaluator_first_name'] = evaluation.evaluator.first_name
                context['evaluator_last_name'] = evaluation.evaluator.last_name
                context['evaluation_status'] = evaluation.status

            return Response(context)

        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

    def get(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do']=="details":
                context['evaluation'] = GetFullEvaluationSerializer(Evaluation.objects.get(id=self.kwargs['evaluation_id'])).data
   
            return Response(context)
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

class DoEvaluationsView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do']=="":
                #context['evaluation'] = GetFullEvaluationSerializer(Evaluation.objects.get(id=self.kwargs['evaluation_id'])).data
                return Response(context)
        except: return Response({'result':'error'})
        return Response({'result':False})


class MyEvaluationView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['which']=="all":
                if isStudent(request.user):
                    evaluations_tmp = Evaluation.objects.filter(student=request.user)
                    if request.query_params.get('where') == "home": 
                        if len(evaluations_tmp)>4: evaluations_tmp = evaluations_tmp[0:4]
                        context['evaluations'] = GetFullEvaluationSerializer(evaluations_tmp, many=True).data
                        return Response(context)
                        
                elif isTeacher(request.user):
                    evaluations_tmp = Evaluation.objects.filter(evaluator=request.user)

                elif isManager(request.user):
                    if request.query_params.get('eid'):
                        evaluations_tmp = Evaluation.objects.filter(exam_id=request.query_params['eid'])
                    else:
                        emr_ids = []
                        emr_tmp = ExamManagerRelation.objects.filter(manager=request.user).values('exam')
                        for i in emr_tmp: emr_ids.append(i['exam'])
                        evaluations_tmp = Evaluation.objects.filter(exam_id__in=emr_ids)
                
                elif isAdmin(request.user):
                    evaluations_tmp = Evaluation.objects.filter(exam_id=request.query_params['eid'])\
                        if request.query_params.get('eid') else Evaluation.objects.all()
                    
                if not request.query_params.get('filter_by')=="false" and not isStudent(request.user):
                    evaluations_tmp = evaluations_tmp.filter(status=request.query_params.get('filter_by'))

                evaluations_tmp_len = len(evaluations_tmp)
                if request.query_params['limit'] == 'NaN': pass
                elif int(request.query_params['limit'])>0:
                    if evaluations_tmp_len < int(request.query_params['limit'])+int(request.query_params['skip']):
                        limit_val = evaluations_tmp_len
                    else: limit_val = int(request.query_params['limit'])+int(request.query_params['skip'])-1
                    context['evaluations'] = GetFullEvaluationSerializer(evaluations_tmp[int(request.query_params['skip'])-1:limit_val], many=True).data
                else:context['evaluations'] = []

                context['total_evaluations'] = evaluations_tmp_len
                return Response(context)
        except KeyboardInterrupt:return Response({'result':'error'})
        return Response({'result':False})
