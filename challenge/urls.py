from django.conf.urls import patterns, url

urlpatterns = patterns('challenge.views',
    url(r'^intro/$', 'intro'),
    url(r'^coup_lettres/$', 'coup_lettres'),
    url(r'^valide_lettres/$', 'valide_lettres'),
    url(r'^valide_chiffres/$', 'valide_chiffres'),
    url(r'^fin/$', 'fin'),
)