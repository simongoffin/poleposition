from django.conf.urls import patterns, url

urlpatterns = patterns('connexion.views',
    url(r'^connexion/$', 'connexion'),
    url(r'^deconnexion/$', 'deconnexion'),
    url(r'^confirmation/$', 'confirmation'),
    url(r'^creation/$', 'creation'),
)
