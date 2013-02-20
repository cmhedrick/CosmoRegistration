from django.shortcuts import render_to_response
import datetime
from models import Consult, TextResponse, Choose, Service

def nextapt_context(request):
    return {'nextapt': "January 3rd",}
