# -*-coding:utf-8-*-

from django import forms
from .models import TestCase


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        exclude = ["create_time"]
