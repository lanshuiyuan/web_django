# helloworld/helloworld/urls.py
from django.conf.urls import url
from django.urls import re_path, path
from hello import views
urlpatterns = [
    url(r'^$', views.index),
    url('^demo$', views.demo,name= "demo_page"),
    url('^home$', views.home,name= "hoem_page"),
    url('^demo/page=(\d+)$', views.page),
    # 匹配archive/2018/10.html
    path("archive/<year>/<month>.html", views.home),
    url(r'^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$', views.home1),
    path("lan/", views.lan),
    path("fenceng/", views.fenceng),
]

