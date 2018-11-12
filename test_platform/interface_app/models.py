from django.db import models
from project_app.models import ProjectManage, Module


# Create your models here.

class TestCase(models.Model):
    """
    用例表
    """
    # project = models.ForeignKey(ProjectManage, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, default="")
    url = models.TextField("URL", default="")
    req_method = models.CharField("方法", max_length=10, default="")
    req_type = models.CharField("参数类型", max_length=10, default="")
    req_header = models.TextField("header", default="")
    req_parameter = models.TextField("参数", default="")
    response_assert = models.TextField("断言", default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name

