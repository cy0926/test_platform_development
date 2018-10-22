# -*-coding:utf-8-*-
from django.urls import path
from project_app import views

urlpatterns = [
    path('project_manage/', views.project_manage),
    path('add_index/', views.add_index),
    path('add_project/', views.add_project),
    path('^edit_project_page/(?P<project_id>[0-9]+)/$', views.edit_project_page, name="edit_project_page"),
    path('^edit_project_action/(?P<project_id>[0-9]+)/$', views.edit_project_action, name="edit_project_action"),
    path('^delete/(?P<project_id>[0-9]+)/$', views.delete_project, name="delete"),
    path('search/', views.search),

]
