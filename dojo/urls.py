from django.urls import re_path, path

from dojo import views
from dojo import views_cbv

urlpatterns=[
    path('new/', views.post_new),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_edit),

    re_path(r'^sum/(?P<numbers>[\d/]+\d+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download),

    path('cbv/list1/', views_cbv.post_list1),
    path('cbv/list2/', views_cbv.post_list2),
    path('cbv/list3/', views.post_list3),
    path('cbv/excel/', views.excel_download),
]

