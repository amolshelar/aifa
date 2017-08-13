"""aifa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from personal import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^personal/Tab1/$', views.Tab1, name='Tab1'),
    url(r'^personal/Tab2/$', views.Tab2, name='Tab2'),
    url(r'^personal/register/$', views.register, name='register'),
    url(r'^personal/register1/$', views.register1, name='register1'),
    url(r'^personal/register2/$', views.register2, name='register2'),
    url(r'^personal/register3/$', views.register3, name='register3'),
]
