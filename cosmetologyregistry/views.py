from django.shortcuts import render_to_response
from models import Consult, TextResponse, Choose, Service

def homepage(request):
    consult = Consult.objects.get(id=1)
    return render_to_response('homepage.html', {'consult': consult})
