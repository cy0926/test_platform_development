# -*-coding:utf-8-*-
from django.urls import path
from interface_app.views import testcase_views

urlpatterns = [
    # 用例管理
    path('case_manage/', testcase_views.case_manage),
    path('add_case/', testcase_views.add_case),
    path('api_debug/', testcase_views.api_debug),
    path('save_case/', testcase_views.save_case),
    path('get_project_list/', testcase_views.get_project_list),
    path('debug_case/<int:case_id>/', testcase_views.debug_case),
    path('search_case_name/', testcase_views.search_case_name),
    path('delete_case/<int:case_id>/', testcase_views.delete_case),
    path('get_case_info/', testcase_views.get_case_info)

]
