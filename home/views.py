from django.template import RequestContext, loader
from django.shortcuts import render_to_response


def index(request):
	return render_to_response('home/index.html', {})


def contact(request):
	return render_to_response('home/contact.html', {})
	
	