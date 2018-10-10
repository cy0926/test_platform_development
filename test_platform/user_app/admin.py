from django.contrib import admin
from user_app.models import ProjectManage, Module


# Register your models here.
# django 自带的一个admin的后台
class ProjectManageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'create_time']
    search_fields = ['title']  # 搜索栏
    list_filter = ['status']  # 过滤器


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'create_time', 'project']


admin.site.register(ProjectManage, ProjectManageAdmin)
admin.site.register(Module, ModuleAdmin)
