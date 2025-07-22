from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class OTP(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=5)

    def check_otp(self, raw_code):
        return check_password(raw_code, self.code)