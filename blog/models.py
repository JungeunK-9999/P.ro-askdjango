#blog-models

import re
from django.db import models
from django.forms import ValidationError
# from django.utils import timezone

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid LngLat Type')

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력하세요.')
    # section = models.CharField(max_length=100,
    #                          choices=(
    #                              ('제목1', '제목1 레이블'),
    #                              ('제목2', '제목2 레이블'),
    #                              ('제목3', '제목3 레이블')
    #                          ))  #길이 제한 있음
    content = models.TextField()              #길이 제한 없음

    tags=models.CharField(max_length=100, blank=True)
    lnglat=models.CharField(max_length=50, blank=True ,
                            validators=[lnglat_validator],
                            help_text='위도/경도 포맷으로 입력하세요',
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


