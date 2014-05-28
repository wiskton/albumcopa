# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from figurinhas.models import Figurinha

def home(request):
    home = True
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def album(request):

    figurinhas = Figurinha.objects.all()
    
    return render_to_response('album.html', locals(), context_instance=RequestContext(request))

def repetidas(request):

    figurinhas = Figurinha.objects.filter(quantidade__gt=0)
    
    return render_to_response('album.html', locals(), context_instance=RequestContext(request))
        