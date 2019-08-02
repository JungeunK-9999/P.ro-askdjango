from django.urls import path, re_path

from . import views_cbv
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('blog/<int:id>', views.post_detail),
    re_path(r'^detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),

    path('new/', views.post_new, name='post_new'),
    path('edit/<int:id>', views.post_edit, name='post_edit'),

    path('cbv/new', views_cbv.post_new),
]

"""
(?P)  정규표현식
\d+    d+패턴에 부합하면
<x>     x라는 변수명으로 인자를 넘기겠다.
"""
