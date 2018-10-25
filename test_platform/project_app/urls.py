# -*-coding:utf-8-*-
from django.urls import path
from project_app.views import project_views

urlpatterns = [
    # 项目管理
    path('project_manage/', project_views.project_manage),
    path('add_project/', project_views.add_project),
    path('edit_project_page/<int:pid>/', project_views.edit_project_page, name="edit_project_page"),
    path('delete/<int:pid>', project_views.delete_project, name="delete"),
    path('search/', project_views.search),

]
