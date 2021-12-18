from django.db.models import F
from auth_api.models import User
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.views import APIView
from auth_api.models import VerificationOTP
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import time, json, datetime, pytz, hashlib, random

jsonDec = json.decoder.JSONDecoder()

ist_tz = pytz.timezone("Asia/Kolkata")

def sendVerificationMail(hostname, _type, user):
    otp = random.randint(100000,999999)
    otp_hash = getMD5(f"{str(otp)}{user.id}")
    veriObj = VerificationOTP(user=user,otp=otp_hash,reason=_type,date_time_expiry=timeAfter(0,0,30))
    veriObj.save()
    mail_msg = f"Hello {user.first_name} {user.last_name}\nPlease Verify Your Email by,\nOTP : {otp}\n\nor\n\nclick on : https://{hostname}/api/auth/verify/email_verification?vk={otp_hash}&uid={user.id}"
    send_mail("Email Verification - MainsIAS", mail_msg,"MainsIAS <accounts@mainsias.com>", [user.email])     
        
def isAdmin(user):
    return True if user.isAdmin else False

def isManager(user):
    return True if user.isManager else False

def isTeacher(user):
    return True if user.isTeacher else False

def isStudent(user):
    return True if user.isStudent else False

def isTopToManagerLevel(user):
    return True if user.isManager or isAdmin(user) else False

def isTopToTeacherLevel(user):
    return True if user.isTeacher or isTopToManagerLevel(user) else False

def isTopToStudentLevel(user):
    return True if user.isStudent or isTopToTeacherLevel(user) else False

def getMD5(data):
    return hashlib.md5(data.encode()).hexdigest()

def timeNow():
    return timezone.localtime()

def timeAfter(days=0,hours=0,minutes=0):
    return datetime.datetime.now()+datetime.timedelta(days=days, hours=hours, minutes=minutes)

def timeBefore(days=0,hours=0,minutes=0):
    return datetime.datetime.now()-datetime.timedelta(days=days, hours=hours, minutes=minutes)

def dateDiff(_from, _to):
    return (_from-_to).days

def json_to_str(value):
    return json.dumps(value)
    
def str_to_json(value):
    return json.loads(value)
    
def list_to_str(value):
    return json.dumps(value)

def str_to_list(value):
    return jsonDec.decode(value)

def getUserFromUsername(username):
    return User.objects.get(username=username)

def getUserFromUid(id):
    return User.objects.get(id=id)

def calculate_from_date(days, frequency):
    if days==0: return timeBefore(0).date()
    elif frequency==1: return timeBefore(0).date()
    elif days<=frequency: return timeBefore(days-1).date()
    else: return calculate_from_date(days-frequency, frequency)

# def UTCtoITC(value):
#     return value.replace(tzinfo=pytz.utc).astimezone(ist_tz)

# async def sendPushNotificaition(uid, data):
#     ep = PushNotificationEndPoint.objects.filter(user=uid).values('endpointdata')
#     if ep:
#         for i in ep:
#             requests.post('http://localhost:8080/push',json={'to':i['endpointdata'],'data':data})

# def setAnActivity(aid, msg):
#     try:
#         Activities(appointment=aid, activity=msg).save()
#         return True
#     except:
#         return False
