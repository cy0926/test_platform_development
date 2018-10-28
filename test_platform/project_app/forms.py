# -*-coding:utf-8-*-

from django import forms
from .models import ProjectManage, Module


# class ProjectForm(forms.Form):
#     title = forms.CharField(label="名称", max_length=100)
#     description = forms.CharField(label="描述", widget=forms.Textarea)
#     status = forms.BooleanField(label="状态")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectManage
        fields = ['title', 'description', 'status']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ['create_time']
