from django.shortcuts import render, render_to_response
from django.template import RequestContext
from web.models import Evento

def home_view(request):
	template = "index.html"
	e = Evento.objects.all()
	ctx = { 'eventos' : e}
	return render_to_response(template, ctx, context_instance=RequestContext(request))

