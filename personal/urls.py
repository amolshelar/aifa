from django.conf.urls import url
from personal import views


urlpatterns=[url(r'^$', views.main, name='main'),
             url(r'^personal/Tab1/$', views.Tab1, name='Tab1'),
	     url(r'^personal/code/$', views.code, name='code'),
             url(r'^personal/register/$', views.code, name='register'), ]
