from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from views import MakeAptView, UpdateUserView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html',}, ),
    url(r'^visit_us/$', TemplateView.as_view(template_name='visit_us.html')),
    url(r'^price_list/$', TemplateView.as_view(template_name='price_list.html')),
    url(r'^curriculum/$', TemplateView.as_view(template_name='curriculum.html')),
    url(r'^additional_classes/$', TemplateView.as_view(template_name='additional_classes.html')),
    url(r'^events/$', TemplateView.as_view(template_name='events.html')),
    url(r'^makeapt/$', login_required(MakeAptView.as_view())),
    url(r'^confirmapt/$', TemplateView.as_view(template_name='confirmapt.html')),
    url(r'^users/(?P<pk>\w+)/$', UpdateUserView.as_view()),
)
