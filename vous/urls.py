from django.conf.urls import patterns, url

urlpatterns = patterns('vous.views',
    url(r'^vous/$', 'vous'),
)