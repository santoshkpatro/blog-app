from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('You are visiting home page')


def contact(request):
    return HttpResponse('You are visiting contact page')


def about(request):
    return HttpResponse('You are visiting about page')