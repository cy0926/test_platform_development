from django.db import models


# Create your models here.

class ProjectManage(models.Model):
    """
    项目表
    """
    title = models.CharField("名称", max_length=100, blank=False, default="")  # 名称
    description = models.TextField("描述", max_length=100, default="")  # 描述
    status = models.BooleanField("status", default=True)  # 状态
    create_time = models.DateTimeField("创建时间", auto_now=True)  # 创建时间

    def __str__(self):
        return self.title


class Module(models.Model):
    """
    模块表

    """
    project = models.ForeignKey(ProjectManage, on_delete=models.CASCADE)
    title = models.CharField("名称", max_length=100, blank=False, default="")  # 名称
    description = models.CharField("描述", max_length=100, default="")  # 描述
    status = models.BooleanField("status", default=True)  # 状态
    create_time = models.DateTimeField("创建时间", auto_now=True)  # 创建时间

    def __str__(self):
        return self.title
