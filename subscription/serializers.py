from .models import Subscription, SubscriptionQuestionAllowence, SubscriptionQuestionCategory, ManagerEdits
from rest_framework import serializers
from auth_api.serializers import UserShortSerializer
import exam
 
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        
class SubscriptionQuestionAllowenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionQuestionAllowence
        fields = '__all__'
    
class GetSubscriptionSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    subscription_allowences = SubscriptionQuestionAllowenceSerializer(read_only=True, many=True)
    class Meta:
        model = Subscription
        fields = '__all__'

class SubscriptionQuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionQuestionCategory
        fields = '__all__'

class GetSubscriptionQuestionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionQuestionCategory
        exclude = ['evaluation_cost']

class ManagerEditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerEdits
        fields = '__all__'

class GetFullManagerEditsSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    created_by = serializers.SerializerMethodField('serializeUser')

    class Meta:
        model = ManagerEdits
        exclude = ['content_bkp']
        
    def serializeUser(self, data):
        return UserShortSerializer(data.created_by).data 

class GetSubscriptionQuestionAllowenceSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('serializeCategory')

    class Meta:
        model = SubscriptionQuestionAllowence
        fields = '__all__'
    
    def serializeCategory(self, data):
        return GetSubscriptionQuestionCategorySerializer(data.category).data

class GetSubscriptionFullSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")  
    created_by = serializers.SerializerMethodField('serializeUser')
    subscription_allowences = GetSubscriptionQuestionAllowenceSerializer(read_only=True, many=True)
    
    class Meta:
        model = Subscription
        fields = '__all__'

    def serializeUser(self, data):
        return UserShortSerializer(data.created_by).data 

class GetSubscriptionFullSerializerwithExam(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")    
    created_by = serializers.SerializerMethodField('serializeUser')
    exam = serializers.SerializerMethodField('serializeExam')
    subscription_allowences = GetSubscriptionQuestionAllowenceSerializer(read_only=True, many=True)

    class Meta:
        model = Subscription
        fields = '__all__'

    def serializeUser(self, data):
        return UserShortSerializer(data.created_by).data 

    def serializeExam(self, data):
        return exam.serializers.ExamShortSerializer(data.exam).data 