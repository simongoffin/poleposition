from django.db import models

class Score(models.Model):
    user_name = models.CharField(max_length=30)
    score = models.IntegerField(verbose_name="Score de la partie")
    temps = models.FloatField(verbose_name="Temps de la partie")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de connexion")
