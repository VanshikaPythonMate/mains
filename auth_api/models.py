from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser): 
    username = None
    isAdmin = models.BooleanField(default=False)
    isManager = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    isTeacher = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=True)
    can_create_subscription = models.BooleanField(default=False)
    defaultExam = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='images/profile', null=True, max_length=100)
    gender = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=254, unique=True)
    created_by = models.ForeignKey("self", null=True, related_name="UserRoleCreatedByWhome", on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        if self.isManager:
            return f"{self.id}, Manager, {self.email}, {self.first_name}"
        elif self.isAdmin:
            return f"{self.id}, Admin, {self.email}, {self.first_name}"
        elif self.isStudent:
            return f"{self.id}, Student, {self.email}, {self.first_name}"
        elif self.isTeacher:
            return f"{self.id}, Teacher, {self.email}, {self.first_name}"
        else: return super().__str__()
        
    class Meta: 
        ordering = ('-id',)

class VerificationOTP(models.Model):

    user = models.ForeignKey(User, related_name="Verification_for_User", on_delete=models.CASCADE)
    otp = models.TextField(null=True)
    reason = models.CharField(max_length=256, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    date_time_expiry = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user.email}, {self.otp}, {self.reason}"

class unverifiedToken(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    unauthtoken=models.CharField(max_length=256)