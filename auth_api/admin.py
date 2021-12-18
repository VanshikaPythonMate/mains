from django.contrib import admin
from .models import User, VerificationOTP
admin.site.register(User)
admin.site.register(VerificationOTP)