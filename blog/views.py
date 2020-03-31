from django.shortcuts import render, HttpResponse

# Create your views here.
def blogPost(request):
    return render(request, 'blog/blogPost.html')
