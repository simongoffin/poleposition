#-*- coding: utf-8 -*-
from django import forms

class LettersForm(forms.Form):
    solution = forms.CharField(label="Solution", max_length=11,required=False)

class ChiffresForm(forms.Form):
    op1 = forms.CharField(label="1.", max_length=18,required=False)
    op2 = forms.CharField(label="2.", max_length=18,required=False)
    op3 = forms.CharField(label="3.", max_length=18,required=False)
    op4 = forms.CharField(label="4.", max_length=18,required=False)
    op5 = forms.CharField(label="5.", max_length=18,required=False)