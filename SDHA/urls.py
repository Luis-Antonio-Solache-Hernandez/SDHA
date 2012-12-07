from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from registration.forms import RegistrationFormUniqueEmail
from main import *
from django.contrib import admin
#from django.contrib.auth import views
admin.autodiscover()

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('main',),
}


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SDHA.views.home', name='home'),
    # url(r'^SDHA/', include('SDHA.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/register/$', 'registration.views.register', {'backend': 'registration.backends.default.DefaultBackend', 'form_class': RegistrationFormUniqueEmail}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/luis/SDHA/carga/', }),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
)
