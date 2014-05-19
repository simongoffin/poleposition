from django.conf.urls import patterns, url

urlpatterns = patterns('game.views',
    url(r'^auteur/$', 'auteur'),
    url(r'^auteur2/$', 'auteur2'),
    url(r'^home/$', 'home'),
    url(r'^ready/$', 'home'),
    url(r'^random$', 'random'),
)