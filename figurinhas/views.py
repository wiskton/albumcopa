# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from figurinhas.models import Figurinha

def home(request):
    home = True
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def album(request):

    figurinhas = Figurinha.objects.all()
    tenho = Figurinha.objects.filter(tenho=True).count()
    faltam = Figurinha.objects.filter(tenho=False).count()
    total = figurinhas.count()
    porcento = tenho * 100 / total
    rp = Figurinha.objects.filter(quantidade__gt=0)
    repetidas = 0
    for r in rp:
        repetidas += r.quantidade
    
    return render_to_response('album.html', locals(), context_instance=RequestContext(request))

def repetidas(request):
    rp = Figurinha.objects.filter(quantidade__gt=0)
    repetidas = 0
    for r in rp:
        repetidas += r.quantidade

    figurinhas = Figurinha.objects.filter(quantidade__gt=0)
    
    return render_to_response('repetidas.html', locals(), context_instance=RequestContext(request))
        