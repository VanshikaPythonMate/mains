from .models import EvaluatorPaymentDetails, EvaluatorGlance, EvaluatorRating
from rest_framework import serializers
from auth_api.serializers import UserShortSerializer

class EvaluatorPaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluatorPaymentDetails
        fields = '__all__'

class GetEvaluatorPaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluatorPaymentDetails
        exclude = ['id',"evaluator"]

class EvaluatorGlanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluatorGlance
        fields = '__all__'

class EvaluatorRatingSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = EvaluatorRating
        fields = '__all__'

class GetEvaluatorRatingSerializer(serializers.ModelSerializer):
    class Meta:

        model = EvaluatorRating
        fields = '__all__'

class GetEvaluatorGlanceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    last_updated = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    evaluator = serializers.SerializerMethodField('serializeEvaluator')
    
    class Meta:
        model = EvaluatorGlance
        exclude = ['closed_details',"closed_at"]

    def serializeEvaluator(self, data):
        return UserShortSerializer(data.evaluator).data 

class GetPreviousEvaluatorGlanceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    last_updated = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    closed_at = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    evaluator = serializers.SerializerMethodField('serializeEvaluator')

    class Meta:
        model = EvaluatorGlance
        fields = '__all__'

    def serializeEvaluator(self, data):
        return UserShortSerializer(data.evaluator).data 