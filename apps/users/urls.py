from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^creating_user/$', views.creating_user,name="creating_user"),
    url(r'^log/$', views.log,name="login"),
    url(r'^logout/$', views.logout,name="logout"),
    url(r'^author/$', views.author,name="author"),
    url(r'^author_creating/$', views.author_creating,name="author_creating"),
]