from .models import Exam, ExamManagerRelation
from rest_framework import serializers
from subscription.serializers import GetSubscriptionFullSerializer, GetSubscriptionSerializer

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class GetExamSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    class Meta:
        model = Exam
        fields = '__all__'

class ExamShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ["short_name", "full_name", "id"]

class GetExamFullSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    
    class Meta:
        model = Exam
        fields = '__all__'

class GetListExamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exam
        fields = ["short_name","image"]

class ExamManagerRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamManagerRelation
        fields = '__all__'

class GetExamManagerRelationSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    class Meta:
        model = ExamManagerRelation
        fields = '__all__'

class GetFullExamManagerRelationSerializer(serializers.ModelSerializer):
    date_time_created = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    class Meta:
        model = ExamManagerRelation
        fields = '__all__'

class GetExamListExamManagerRelationSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField('serializeExam')

    class Meta:
        model = ExamManagerRelation
        exclude = ("manager","date_time_created","active",'id')

    def serializeExam(self, data):
        return ExamShortSerializer(data.exam).data




