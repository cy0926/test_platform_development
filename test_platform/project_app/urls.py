#-*-coding:utf-8-*-
from django.urls import path
from project_app import views

urlpatterns = [
    path('project_manage/', views.project_manage),

    ]