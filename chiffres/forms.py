#-*- coding: utf-8 -*-
from django import forms

class ChiffresForm(forms.Form):
    arg1 = forms.IntegerField(label="*",min_value=1, max_value=99)
    arg2 = forms.IntegerField(label="*",min_value=1, max_value=99)
    arg3 = forms.IntegerField(label="*",min_value=1, max_value=99)
    arg4 = forms.IntegerField(label="*",min_value=1, max_value=99)
    arg5 = forms.IntegerField(label="*",min_value=1, max_value=99)
    arg6 = forms.IntegerField(label="*",min_value=1, max_value=99)
    arg7 = forms.IntegerField(label="compte",min_value=1, max_value=999)
