from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_agent = models.CharField(max_length=200)


class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices=(
                                       ('A', 'A서버'),
                                       ('B', 'B서버'),
                                       ('C', 'C서버'),
                                   ))
    username=models.CharField(max_length=10, validators=[MinLengthValidator(3)])

    class Meta:
        unique_together=[
            ('server_name', 'username'),
        ]