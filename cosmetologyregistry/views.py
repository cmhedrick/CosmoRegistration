from django.shortcuts import render_to_response
import datetime
from models import Consult, TextResponse, Choose, Service, Appointment

def nextapt_context(request):
    apt = Appointment.objects.filter(
        user=request.user
    ).filter(
        date_time__gte=datetime.datetime.now()
    )
    if apt:
        dt = apt[0].date_time.strftime("%b %e %I:%M %p")
    else:
        dt = "no appointment"
    return {'nextapt': dt,}
