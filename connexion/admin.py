# -*- coding:utf-8 -*-
from django.contrib import admin
from connexion.models import Connexion

class ConnexionAdmin(admin.ModelAdmin):
    list_display   = ('user_name','date','nb_run_lettres','nb_run_chiffres')


admin.site.register(Connexion,ConnexionAdmin)

