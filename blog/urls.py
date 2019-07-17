
from django.urls import path
from . import views
app_name='blog'
urlpatterns=[
    path('', views.post_list, name='blog'),
]

"""
(?P)  정규표현식
\d+    d+패턴에 부합하면
<x>     x라는 변수명으로 인자를 넘기겠다.
"""