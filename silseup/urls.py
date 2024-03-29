"""silseup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.views.generic import RedirectView


def root(request):
    return redirect('blog:post_list')


urlpatterns = [
    # path('', root),
    # path('', lambda r: redirect('blog:post_list')),
    path('', RedirectView.as_view(pattern_name='blog:post_list'), name="root"),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('dojo/', include('dojo.urls')),
    # re_path(r'^dojo/', include('dojo.urls.py')),
    path('shop/', include('shop.urls')),

]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)), ]
