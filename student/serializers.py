from .models import StudentSubscriptionRecord, StudentSubscriptionsQuestionsRecord
from rest_framework import serializers
from mainsias_dj.easy import timeNow
from exam.serializers import ExamShortSerializer
from subscription.serializers import GetSubscriptionQuestionCategorySerializer

class StudentSubscriptionsQuestionsRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubscriptionsQuestionsRecord
        fields = '__all__'

class GetStudentSubscriptionsQuestionsRecordSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('serializeCategory')
    class Meta:
        model = StudentSubscriptionsQuestionsRecord
        fields = '__all__'

    def serializeCategory(self, data):
        return GetSubscriptionQuestionCategorySerializer(data.category).data

class StudentSubscriptionRecordSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('serializeCategory')
    class Meta:
        model = StudentSubscriptionRecord
        fields = '__all__'
    
    def serializeCategory(self, data):
        return GetSubscriptionQuestionCategorySerializer(data.category).data

class GetStudentSubscriptionRecordSerializer(serializers.ModelSerializer):
    student_subscribed_allowences = StudentSubscriptionsQuestionsRecordSerializer(read_only=True, many=True)
    purchase_time = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    expiry_date = serializers.DateField(format="%d-%b-%Y")
    is_expired = serializers.SerializerMethodField('isExpired')

    class Meta:
        model = StudentSubscriptionRecord
        fields = '__all__'

    def isExpired(self, data):
        return False if data.expiry_date>timeNow().date() else True

class GetStudentSubscriptionRecordFullSerializer(serializers.ModelSerializer):
    student_subscribed_allowences = StudentSubscriptionsQuestionsRecordSerializer(read_only=True, many=True)
    purchase_time = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    expiry_date = serializers.DateField(format="%d-%b-%Y")
    exam = serializers.SerializerMethodField('serializeExam')
    is_expired = serializers.SerializerMethodField('isExpired')

    class Meta:
        model = StudentSubscriptionRecord
        fields = '__all__'

    def isExpired(self, data):
        return False if data.expiry_date>timeNow().date() else True

    def serializeExam(self, data):
        return ExamShortSerializer(data.exam).data 
