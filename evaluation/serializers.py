from .models import Evaluation
from rest_framework import serializers
from exam.serializers import ExamShortSerializer
from auth_api.serializers import UserShortSerializer
from student.serializers import GetStudentSubscriptionRecordFullSerializer, GetStudentSubscriptionsQuestionsRecordSerializer

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class GetEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class GetShortEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ["id","student","evaluator","exam","subscribed_subscription","answer_file","answers_count","tags","date","time"]

class GetEvaluationSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%b-%Y")
    time = serializers.TimeField(format="%H:%M")
    date_time_recent = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    date_time_evaluated = serializers.DateTimeField(format="%d-%b-%Y %H:%M")

    class Meta:
        model = Evaluation
        fields = '__all__'

class GetFullEvaluationSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%b-%Y")
    time = serializers.TimeField(format="%H:%M")
    date_time_recent = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    date_time_evaluated = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    student = serializers.SerializerMethodField('serializeStudent')
    evaluator = serializers.SerializerMethodField('serializeEvaluator')
    exam = serializers.SerializerMethodField('serializeExam')
    subscribed_subscription = serializers.SerializerMethodField('serializeSubscribedSubscription')
    subject = GetStudentSubscriptionsQuestionsRecordSerializer(read_only=True)
    
    class Meta:
        model = Evaluation
        fields = '__all__'

    def serializeStudent(self, data):
        return UserShortSerializer(data.student).data 
    
    def serializeEvaluator(self, data):
        return UserShortSerializer(data.evaluator).data 
    
    def serializeExam(self, data):
        return ExamShortSerializer(data.exam).data 
    
    def serializeSubscribedSubscription(self, data):
        return GetStudentSubscriptionRecordFullSerializer(data.subscribed_subscription).data 