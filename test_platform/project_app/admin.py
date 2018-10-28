from django.contrib import admin
from project_app.models import ProjectManage, Module


# Register your models here.

class ProjectManageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'create_time']
    search_fields = ['title']  # 搜索栏
    list_filter = ['status']  # 过滤器


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'create_time', 'project']


admin.site.register(ProjectManage, ProjectManageAdmin)
admin.site.register(Module, ModuleAdmin)
