from django.shortcuts import render_to_response
import datetime
from dateutil import parser
from django.contrib.auth.models import User
from models import Consult, TextResponse, Choose, Service, Appointment
from django.views.generic import FormView, UpdateView
from django.forms import ModelForm

def nextapt_context(request):
    if request.user.is_authenticated():
        apt = Appointment.objects.filter(
            user=request.user
        ).filter(
            date_time__gte=datetime.datetime.now()
        ).order_by(
            'date_time'
        )
        if apt:
            dt = apt[0].date_time.strftime("%b %e %I:%M %p")
        else:
            dt = "no appointment"
    else:
        dt = ""
    return {'nextapt': dt,}

class MakeAptForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ['user']

class MakeAptView(FormView):
    template_name = 'makeapt.html'
    form_class = MakeAptForm

    def get_context_data(self, **kwargs):
        context = super(MakeAptView, self).get_context_data(**kwargs)
        if "makeapt_form" not in context:
            context['makeapt_form'] = MakeAptForm()
        return context

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        dt = parser.parse(form.data['date_time'])
        apt = Appointment(user=self.request.user, date_time=dt)
        apt.save()
        return super(MakeAptView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(makeapt_form=form))

class UpdateUserForm(ModelForm):
    class Meta:
        model = User

class UpdateUserView(UpdateView):
    form_class = UpdateUserForm
    model = User
    template_name = 'update_user.html'
    
    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = User.objects.get(username=self.kwargs['pk'])
        return obj
