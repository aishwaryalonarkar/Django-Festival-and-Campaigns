# -*- coding: utf-8 -*-
from django import forms

class NameForm(forms.Form):
    obj = forms.CharField(label='Your obj', max_length=100)