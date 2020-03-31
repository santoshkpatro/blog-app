from django.shortcuts import render, HttpResponse

# Create your views here.
def blogPost(request):
    return HttpResponse('You are visiting blogPost')
