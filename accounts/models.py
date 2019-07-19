from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # FIXME : BAD CASE!!!

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)