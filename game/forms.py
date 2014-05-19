#-*- coding: utf-8 -*-
from django import forms

class LettersForm(forms.Form):
    arg1 = forms.CharField(label="*", max_length=1,required=False)
    arg2 = forms.CharField(label="*", max_length=1,required=False)
    arg3 = forms.CharField(label="*", max_length=1,required=False)
    arg4 = forms.CharField(label="*", max_length=1,required=False)
    arg5 = forms.CharField(label="*", max_length=1,required=False)
    arg6 = forms.CharField(label="*", max_length=1,required=False)
    arg7 = forms.CharField(label="*", max_length=1,required=False)
    arg8 = forms.CharField(label="*", max_length=1,required=False)
    arg9 = forms.CharField(label="*", max_length=1,required=False)
