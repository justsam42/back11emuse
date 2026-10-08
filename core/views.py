from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.

####----------------API Rest Views for db objects

@api_view(["GET", "POST"])
def text(request, format=None):

    if request.method=="GET":
        selection = Text.objects.all()
        serializer = TextSerializer(selection, many=True)

        return Response({ 
            "texts" : serializer.data
        })
    
    if request.method=="POST":
        newText = TextSerializer(data=request.data)
        
        if newText.is_valid():
            newText.save()

        return Response(newText.data, status=status.HTTP_201 )

####----------------Django Classic Views  

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