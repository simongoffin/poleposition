#-*- coding: utf-8 -*-
from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=20)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class ProfilForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=20)
    email=forms.CharField(label="Adresse e-mail", max_length=75)
    #password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
    