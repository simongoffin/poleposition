from django.conf.urls import patterns, url

urlpatterns = patterns('chiffres.views',
    url(r'^home/$', 'home'),
    url(r'^random$', 'random'),
)
