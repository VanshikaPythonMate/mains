from .models import User
from rest_framework import serializers


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name","last_name","email","phone"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GetUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d-%b-%Y %H:%M")
    
    class Meta:
        model = User
        exclude = ('password','user_permissions','groups','is_staff','is_superuser',)
