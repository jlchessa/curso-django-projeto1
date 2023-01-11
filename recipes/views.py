from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'João Chessa',
    })


def contact(request):
    return HttpResponse('Contato')


def about(request):
    return HttpResponse('Sobre')
