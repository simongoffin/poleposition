# -*- coding:utf-8 -*-
from django.contrib import admin
from challenge.models import Score

class ScoreAdmin(admin.ModelAdmin):
    list_display   = ('user_name','score','temps','date')


admin.site.register(Score,ScoreAdmin)
