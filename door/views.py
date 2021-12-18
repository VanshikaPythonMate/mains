from mainsias_dj.easy import *
from .models import NoticeBoard, TermsnConditions
from auth_api.models import User
from exam.models import Exam

class DoGeneral(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def get(self, request, *args, **kwargs):
        context = {}
        if self.kwargs['do'] == "get-notices":
            notices = NoticeBoard.objects.all().values('notice')
            notices_final = []
            for i in notices:
                notices_final.append(i['notice'])
            if len(notices_final)>5: notices_final = notices_final[0:5]
            return Response({"notices":notices_final})

        elif self.kwargs['do'] == "get-admin-dash" and isAdmin(request.user):
            all_users = User.objects.all()
            context['students_count'] = all_users.filter(isStudent=True).count()
            context['evaluators_count'] = all_users.filter(isTeacher=True).count()
            context['managers_count'] = all_users.filter(isManager=True).count()
            context['exams_count'] = Exam.objects.all().count()
        return Response(context)

    def post(self, request, *args, **kwargs):
        context = {'result':True}
        if self.kwargs['do'] == 'update-user-profile':
            user = User.objects.get(id=request.user.id)
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.gender = request.data['gender']
            user.phone = request.data['phone']
            user.save()
            context['first_name'] = user.first_name
            context['last_name'] = user.last_name
            context['gender'] = user.gender
            context['phone'] = user.phone
        return Response(context)

class DoPublic(APIView):

    def get(self, request, *args, **kwargs):
        context = {'result':True}
        if self.kwargs['do'] == "get-tnc":
            context['tnc_list'] = TermsnConditions.objects.all().values('note',"is_heading")
            return Response(context)
