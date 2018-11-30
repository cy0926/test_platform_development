# -*-coding:utf-8-*-
from django.urls import path
from interface_app.views import testcase_views, testcase_api

urlpatterns = [
    # 用例管理
    path('case_manage/', testcase_views.case_manage),
    path('add_case/', testcase_views.add_case),

    path('save_case/', testcase_api.save_case),

    path('debug_case/<int:case_id>/', testcase_views.debug_case),
    path('search_case_name/', testcase_views.search_case_name),
    path('delete_case/<int:case_id>/', testcase_views.delete_case),


    # 用例管理 -- 由JS调用的接口
    path('api_debug/', testcase_api.api_debug),
    path('get_project_list/', testcase_api.get_project_list),
    path('get_case_info/', testcase_api.get_case_info),
    path('api_assert/', testcase_api.api_assert),
    path('update_case/', testcase_api.update_case),

]
