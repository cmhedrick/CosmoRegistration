from django.shortcuts import render_to_response
import datetime
from dateutil import parser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from models import UserProfile, Consult, TextResponse, Choose, Service, Appointment
from django.views.generic import FormView, UpdateView
from django.forms import ModelForm, Form, CharField

PASSWORD_MISMATCH = 'Username and Password do not match'
USERNAME_TAKEN = 'Username is taken. Please choose another'
PASSWORD_CONFIRM_MISMATCH = 'Password and Confirm Password do not match'

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
            dt = ""
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
        return '/confirmapt?apt=%s' % self.dt 

    def form_valid(self, form):
        dt = parser.parse(form.data['date_time'])
        self.dt = dt.strftime("%b %e %I:%M %p")
        apt = Appointment(user=self.request.user, date_time=dt)
        apt.save()
        return super(MakeAptView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(makeapt_form=form))

class UpdateUserForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ["user"]

class UpdateUserView(UpdateView):
    form_class = UpdateUserForm
    model = UserProfile
    template_name = 'update_user.html'
    
    def get(self, request, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.kwargs['pk'])
        objlist = UserProfile.objects.filter(user=user)
        if objlist:
            return objlist[0] 
        obj = UserProfile(user=user)
        obj.save()
        return obj

    def get_success_url(self):
        return '/'

class LoginForm(Form):
    new_first_name = CharField(label='Your first name')
    new_last_name = CharField(label='Your last name')
    new_username = CharField(label='Your username')
    new_password = CharField(label='Your password')
    new_password_confirm = CharField(label='Confirm password')
    existing_username = CharField(label='Your username')
    existing_password = CharField(label='Your password')

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if 'register-button' in self.data:
            if 'existing_username' in self.errors:
                del self.errors['existing_username']
            if 'existing_password' in self.errors:
                del self.errors['existing_password']
            if self.is_valid():
                objlist = User.objects.filter(username=self.data['new_username'])
                if objlist:
                    self.errors['new_username'] = USERNAME_TAKEN
                else:
                    if self.data['new_password'] != self.data['new_password_confirm']:
                        self.errors['new_password_confirm'] = PASSWORD_CONFIRM_MISMATCH
        elif 'login-button' in self.data:
            if 'new_first_name' in self.errors:
                del self.errors['new_first_name']
            if 'new_last_name' in self.errors:
                del self.errors['new_last_name']
            if 'new_username' in self.errors:
                del self.errors['new_username']
            if 'new_password' in self.errors:
                del self.errors['new_password']
            if 'new_password_confirm' in self.errors:
                del self.errors['new_password_confirm']
            if self.is_valid():
                objlist = User.objects.filter(username=self.data['existing_username'])
                if objlist:
                    user = objlist[0]
                    if user.check_password(self.data['existing_password']):
                        return cleaned_data
                self.errors['existing_username'] = PASSWORD_MISMATCH
        return cleaned_data

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return '/' 

    def form_valid(self, form):
        if 'register-button' in form.data:
            username = form.data['new_username']
            password = form.data['new_password']
            user = User.objects.create_user(username, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            login(self.request, user)
        elif 'login-button' in form.data:
            username = form.data['existing_username']
            password = form.data['existing_password']
            user = authenticate(username=username, password=password)
            login(self.request, user)
        return super(LoginView, self).form_valid(form)
