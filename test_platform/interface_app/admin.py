from django.contrib import admin
from interface_app.models import TestCase


# Register your models here.

class TestCaseAdmin(admin.ModelAdmin):
    list_display = ["module", "name", "url", "req_method", "req_type",
                    "req_header", "req_parameter", "response_assert", "creat_time"]


admin.site.register(TestCase, TestCaseAdmin)
