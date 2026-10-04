from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["GET", "POST"])
def indexHome2(request, format=None):
    if request.method=="POST":
        pass

    if request.method=="GET":
        return render(request, "index.html")
    

def indexHome(request):
    return render(request, "core/index.html")

def aboutPage(request):
    return render(request, "core/about.html")

def solutionsPage(request):
    return render(request, "core/services.html")

def servicePage(request):
    return render(request, "core/service.html")

def ideePage(request):
    return render(request, "core/idee.html")

def projetPage(request):
    return render(request, "core/projet.html")

def contactPage(request):
    return render(request, "core/contact.html")