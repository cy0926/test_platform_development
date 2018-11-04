# -*-coding:utf-8-*-
from django.urls import path
from interface_app import views

urlpatterns = [
    # 用例管理
    path('case_manage/', views.case_manage),

]
