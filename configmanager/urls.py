from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^template/$', views.template, name='template'),
    url('^template/render/', views.render, name='render'),
 #   url(r'^myForm/$', views.get_name, name='myForm'),
 #   url(r'^configForm/$', views.dform, name='configForm')
]