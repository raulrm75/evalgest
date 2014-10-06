from django.conf.urls import patterns, url
from preeval import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )

