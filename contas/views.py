# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def paginaInicial(request):
    return HttpResponse("Bem vindo a pagina do app de contas")
