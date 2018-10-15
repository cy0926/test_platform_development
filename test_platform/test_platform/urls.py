"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('accounts/login/', views.index),
    path('login_action/', views.login_action),
    path('manage/', include('project_app.urls')),
    # path('project_manage/', views.project_manage),
    path('logout/', views.logout),
    path('search/', views.search),
    path('add_index/', views.add_index),
    path('add_project/', views.add_project),
    path('^delete/(?P<project_id>[0-9]+)/$', views.delete_project, name="delete"),
    path('^edit_project_page/(?P<project_id>[0-9]+)/$', views.edit_project_page, name="edit_project_page"),
    path('^edit_project_action/(?P<project_id>[0-9]+)/$', views.edit_project_action, name="edit_project_action")


]
