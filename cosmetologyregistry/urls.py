from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
)
