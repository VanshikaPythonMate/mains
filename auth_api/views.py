from mainsias_dj.easy import *
from django.shortcuts import redirect
from auth_api.models import User, VerificationOTP
from django.contrib.auth.hashers import make_password, check_password
from auth_api.serializers import UserSerializer, GetUserSerializer
from rest_framework.authtoken.models import Token
from student.views import addRegistrationFreeBenifits

class Signin(APIView):

    def post(self, request, *args, **kwargs):
        context = {'result':True}
        try:
            user = User.objects.filter(email=request.data['username'],is_active=True)
            print(user)
            if not user: return Response({'result':'nouser'})
            else: user=user[0]
            if not check_password(request.data['password'],user.password): return Response({'result':'invalid'})
            token = Token.objects.filter(user=user)
            if token:
                token = token[0]
            else:
                token = Token.objects.create(user=user)
            context['token'] = token.key
            context['user'] = GetUserSerializer(token.user).data
        except: context['result'] = 'error'
        return Response(context)


class Signup(APIView):

    def post(self, request, *args, **kwargs):
        context = {'result':True}
        rd = request.data
        try:
            if User.objects.filter(email=rd['email']): return Response({'result':"exist"})
            user = User.objects.create(first_name=rd['first_name'].title(),last_name=rd['last_name'].title(),email=rd['email'],\
                password=make_password(rd['password']),isStudent=True, isVerified=False)
            user.is_active=False
            user.save()
            sendVerificationMail(request.META['HTTP_HOST'],'email_verification',user)
            token = Token.objects.create(user=user)
            context['token'] = token.key
            context['user'] = GetUserSerializer(token.user).data
        except KeyboardInterrupt:
            context['result'] = 'error'
        return Response(context)

class Verify(APIView):

    def post(self, request, *args, **kwargs):
        context = {'result':True}
        try:
            if self.kwargs['type'] == 'forgot-password':
                if request.data.get('do') == "send-otp":
                    user = User.objects.filter(email=request.data['email'])
                    if not user: return Response({'result':'invalid'})
                    otp = random.randint(100000,999999)
                    do_resend = VerificationOTP.objects.filter(user=user[0],reason=self.kwargs['type']) 
                    if do_resend:
                        do_resend[0].otp = otp
                        do_resend[0].date_time_expiry=timeAfter(0,0,30)
                        do_resend[0].save()
                    else: VerificationOTP(user=user[0],otp=otp,reason=self.kwargs['type'],date_time_expiry=timeAfter(0,0,30)).save()
                    mail_msg = f"Hello {user[0].first_name} {user[0].last_name}\nPlease Verify Your Email by,\nOTP : {otp}\n\n"
                    send_mail("Forgot Password - MainsIAS", mail_msg,"MainsIAS <accounts@mainsias.com>", [user[0].email],fail_silently=True)
                    return Response(context)

                elif request.data.get('do') == "update-password":
                    user = User.objects.get(email=request.data['email'])
                    otp_obj = VerificationOTP.objects.filter(user=user,otp=request.data['otp'],reason=self.kwargs['type'])
                    if not otp_obj: return Response({'result':'invalid'})
                    user.password = make_password(request.data['password'])
                    user.save()
                    return Response(context)

            elif self.kwargs['type'] == 'email_verification':
                user = Token.objects.get(key=request.data['token']).user
                if request.data.get('do') == "resend":
                    VerificationOTP.objects.filter(user=user, reason=self.kwargs['type']).delete()
                    sendVerificationMail(request.META['HTTP_HOST'],'email_verification',user)
                    return Response(context)
                else:
                    otp_hash = getMD5(f"{str(request.data['otp'])}{user.id}")
                    verfication_obj = VerificationOTP.objects.get(otp=otp_hash)
                    if not verfication_obj:
                        return Response({'reason':False})
                    if self.kwargs['type'] == 'email_verification':
                        addRegistrationFreeBenifits(user.id)
                        verfication_obj.delete()
                        user.isVerified = True
                        user.is_active=True; user.save()
                    return Response(context)
        except KeyboardInterrupt:pass
        return Response({'result':False})
        
    def get(self, request, *args, **kwargs):
        context = {'result':True}
        rg = request.GET
        try:
            veriObj = VerificationOTP.objects.filter(otp=rg['vk'],reason=self.kwargs['type'])
            if self.kwargs['type'] == 'email_verification':
                addRegistrationFreeBenifits(User.id)
                veriObj.delete()
                user = veriObj[0].user; user.isVerified = True; user.save()
            return redirect('https://mainsias.com')
        except :pass
        return Response({'result':False})

class ValidateToken(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = Token.objects.get(key=request.data.get('token')).user
            if user:
                return Response({'result':True,'token':request.data.get('token'),'user':GetUserSerializer(user).data})
        except: pass
        return Response({'result':False})

class ChangePassword(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.user.id)
            if not check_password(request.data['current'],user.password): return Response({'result':'invalid_current_password'})
            user.password=make_password(request.data['new'])
            user.save()
            return Response({'result':True})
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})
        

class DoUser(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def delete(self, request, *args, **kwargs):
        try:
            if self.kwargs['do'] == "delete" and isAdmin(request.user):
                Token.objects.filter(user_id=self.kwargs['uid']).delete()
                User.objects.filter(id=self.kwargs['uid']).delete()
            return Response({'result':True})
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})    

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do'] == "update-active" and isAdmin(request.user):
                user = User.objects.get(id=self.kwargs['uid'])
                user.is_active = request.data['is_active']
                user.save()
                Token.objects.filter(user_id=self.kwargs['uid']).delete()
                context['is_active'] = user.is_active
                context['id'] = user.id
            
            elif self.kwargs['do'] == "update-can_create_subscription" and isAdmin(request.user):
                user = User.objects.get(id=self.kwargs['uid'])
                user.can_create_subscription = request.data['can_create_subscription']
                user.save()
                context['can_create_subscription'] = user.can_create_subscription
                context['id'] = user.id

            return Response(context)
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

    def get(self, request, *args, **kwargs):
        try:
            if self.kwargs['do'] == "get-can_create_subscription" and isTopToManagerLevel(request.user):
                return Response({
                    'result':True,
                    "can_create_subscription":User.objects.get(id=self.kwargs['uid']).can_create_subscription
                })
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})    

class Do(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    

    def post(self, request, *args, **kwargs):
        try:
            context = {'result':True}
            if self.kwargs['do'] == "update-active" and isAdmin(request.user):
                pass

            return Response(context)
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})

    def get(self, request, *args, **kwargs):
        try:
            if self.kwargs['do'] == "get-can_create_subscription" and isTopToManagerLevel(request.user):
               pass
        except KeyboardInterrupt: return Response({'result':'error'})
        return Response({'result':False})    