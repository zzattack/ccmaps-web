from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext, Context
from coffin.shortcuts import render_to_response
from django.core.mail import send_mail
from django.core.exceptions import *
from models import *
from datetime import datetime

# Create your views here.


def version_check(request):
    latest = ProgramVersion.objects.all().order_by('-version')[0]
    template_vars = { 
                     'version': latest.version,
                     'release_date': latest.release_date,
                     'release_notes': latest.release_notes,
                     'url': latest.file.url,
                     }
    
    return render_to_response('tool/version_check.xml', template_vars, mimetype="text/xml")

def get_latest(request):
    latest = ProgramVersion.objects.all().order_by('-version')[0]
    return HttpResponseRedirect(latest.file.url)
