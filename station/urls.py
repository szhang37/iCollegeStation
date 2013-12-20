from django.conf.urls import patterns, url
from station import views
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^courses/item', views.course, name='courseitem'),
        url(r'^courses/', views.courses, name='course'),
        url(r'^school/', views.school, name='school'),
        url(r'^category/', views.category, name='category'),
        url(r'^about/', views.about, name='about'))
