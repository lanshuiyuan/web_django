# helloworld/helloworld/urls.py
from django.conf.urls import url
from django.urls import re_path, path
from hello import views
urlpatterns = [
    url(r'^$', views.index),
    url('^demo$', views.demo),
    url('^demo/page=(\d+)$', views.page),
]
