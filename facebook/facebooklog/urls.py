from django.conf.urls import url,include
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'^fberror/', views.error,name="errorpage"),
    url(r'^success/', views.success,name="success"),
    url(r'^fberror2/', views.error2,name="errorpage2"),
    url(r'^insert/', views.insert,name="errorpage2")



]