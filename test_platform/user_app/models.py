from django.db import models


# Create your models here.
# ORM 创建数据库表
# 操作数据 ORM 以编程的方式来定义操作数据库

# 项目管理表
class ProjectManage(models.Model):
    title = models.CharField(max_length=100)  # 名称
    description = models.CharField(max_length=100)  # 描述
    status = models.BooleanField()  # 状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return self.title
