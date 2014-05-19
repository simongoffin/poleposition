from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Letters.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'connexion.views.connexion'),
    url(r'^game/', include('game.urls')),
    url(r'^chiffres/', include('chiffres.urls')),
    url(r'^connexion/', include('connexion.urls')),
    url(r'^challenge/', include('challenge.urls')),
    url(r'^score/', include('score.urls')),
    url(r'^vous/', include('vous.urls')),
)
