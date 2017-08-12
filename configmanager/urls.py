from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.template, name='index'),
    url(r'^render/$', views.render, name='render'),
    url(r'^get/$', views.getTemplate, name='get'),
 #   url(r'^myForm/$', views.get_name, name='myForm'),
 #   url(r'^configForm/$', views.dform, name='configForm')
]