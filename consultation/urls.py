from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from consultation.models import Consult, TextResponse, Choose

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Consult.objects.all(),
            context_object_name='consullinks',
            template_name='consultation/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Consult,
            template_name='consultation/consulting.html')),
    url(r'^(?P<pk>\d+)/answers/$',
        DetailView.as_view(
            model=Consult,
            template_name='consultation/answers.html'),
        name='consultation_answers'),
    url(r'^(?P<consult_id>\d+)/cast/$', 'consultation.views.cast'),
)
