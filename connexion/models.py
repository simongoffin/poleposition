from django.db import models

class Connexion(models.Model):
    user_name = models.CharField(max_length=20)
    nb_run_lettres = models.IntegerField(verbose_name="Nombre de run en lettres")
    nb_run_chiffres = models.IntegerField(verbose_name="Nombre de run en chiffres")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de connexion")
