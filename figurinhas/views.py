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
    rp = figurinhas.filter(quantidade__gt=0)
    repetidas = 0
    for r in rp:
        repetidas += r.quantidade

    if request.GET.get('q'):
        figs = request.GET.get('q').upper().split(' ')
        encontrados = figurinhas.filter(nome__in=figs, tenho=True).count()

    return render_to_response('album.html', locals(), context_instance=RequestContext(request))

def faltam(request):
    figurinhas = Figurinha.objects.all()
    total = figurinhas.count()

    figurinhas = figurinhas.filter(tenho=False)
    faltam = figurinhas.count()
    
    porcento = faltam * 100 / total

    if request.GET.get('q'):
        figs = request.GET.get('q').upper().split(' ')
        encontrados = figurinhas.filter(nome__in=figs).count()
    
    return render_to_response('faltam.html', locals(), context_instance=RequestContext(request))

def repetidas(request):
    figurinhas = Figurinha.objects.filter(tenho=True)
    repetidas = 0
    for r in figurinhas:
        repetidas += r.quantidade

    if request.GET.get('q'):
        figs = request.GET.get('q').upper().split(' ')
        encontrados = figurinhas.filter(nome__in=figs).count()
    
    return render_to_response('repetidas.html', locals(), context_instance=RequestContext(request))
        