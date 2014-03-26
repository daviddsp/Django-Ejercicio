from django.conf.urls import * #patterns, include, url
from mysite.views import horaActual, horas, listamusicos
from mysite.suma import Suma

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hora/$', horaActual),
    url(r'^suma/$', Suma),
    url(r'^horasfutura/(\d{1,2})/$', horas),
    url(r'^musicos/$', listamusicos),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
