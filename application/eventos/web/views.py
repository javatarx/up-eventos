from django.shortcuts import render_to_response
from django.template import RequestContext
from web.models import Evento

def home_view(request):
    template = "index.html"
    e = Evento.objects.order_by('-fecha_registro')[:3]
    ctx = { 'eventos' : e}
    return render_to_response(template, ctx, context_instance=RequestContext(request))

def deportes_view(request):
    mensaje = "esto es un mensaje desde mis deportes"
    ctx = {'msg':mensaje}
    return render_to_response('deportes.html',ctx, context_instance=RequestContext(request))
