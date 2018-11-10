# -*-coding:utf-8-*-
from django.urls import path
from interface_app.views import testcase_views

urlpatterns = [
    # 用例管理
    path('case_manage/', testcase_views.case_manage),
    path('debug/', testcase_views.debug),
    path('api_debug/', testcase_views.api_debug),
    path('save_case/', testcase_views.save_case),
    path('get_project_list/', testcase_views.get_project_list),

]
