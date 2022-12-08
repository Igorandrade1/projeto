from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Igor Andrade'
    })


def contact(request):
    return render(request, 'temp/temp.html')


def about(request):
    return HttpResponse('about page')
