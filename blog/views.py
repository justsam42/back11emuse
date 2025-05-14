from django.shortcuts import render

# Create your views here.


def indexBlog(request):
    return render(request, "blog/index.html")