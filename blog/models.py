#blog-models

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력하세요.')
    # section = models.CharField(max_length=100,
    #                          choices=(
    #                              ('제목1', '제목1 레이블'),
    #                              ('제목2', '제목2 레이블'),
    #                              ('제목3', '제목3 레이블')
    #                          ))  #길이 제한 있음
    content = models.TextField()              #길이 제한 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


