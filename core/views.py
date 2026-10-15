from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


from core.static.core.data.population.lists.classes import classes
from core.static.core.data.population.lists.categories import categories
from core.static.core.data.population.lists.foundations import natures, types

# Create your views here.

####----------------API Rest Views for db objects

  
objets = [
    {
        "name" : "Natures",
        "location" : "nature",
        "content" : natures
    },
    {
        "name" : "Types",
        "location" : "type",
        "content" : types,
    },
    {
        "name" : "Classes",
        "location" : "classe",
        "content" : classes,
    },
    {
        "name" : "Categories",
        "location" : "categorie",
        "content" : categories
    }
]

def api_test(request):
    ...

def api_index(request):
    return render(request, "core/api/index.html", 
        {
            "objets" : objets
        }
    )

def objet(request, name=""):

    objet = {}
    message = ""

    for i in objets: 

        if i["location"] == name:
            objet = i
        else :
            message = "No object found."

    return render(request, "core/api/objet.html", 
        {
            "filters" : objets,
            "objet" : objet,
            "message" : message
        }
    )

""" 
@api_view(["GET", "POST"])
def natures(request, format=None):

    if request.method=="GET":
        selection = Nature.objects.all()
        serializer = NatureSerializer(selection, many=True)

        return Response({ 
            "natures" : serializer.data
        })
    
    if request.method=="POST":
        newNature = NatureSerializer(data=request.data)
        
        if newNature.is_valid():
            newNature.save()

        return Response(newNature.data, status=status.HTTP_201 )


@api_view(["GET", "POST"])
def types(request, format=None):

    if request.method=="GET":
        selection = Type.objects.all()
        serializer = TypeSerializer(selection, many=True)

        return Response({ 
            "types" : serializer.data
        })
    
    if request.method=="POST":
        newType = TypeSerializer(data=request.data)
        
        if newType.is_valid():
            newType.save()

        return Response(newType.data, status=status.HTTP_201 )


@api_view(["GET", "POST"])
def classes(request, format=None):

    if request.method=="GET":
        selection = Classe.objects.all()
        serializer = ClasseSerializer(selection, many=True)

        return Response({ 
            "classes" : serializer.data
        })
    
    if request.method=="POST":
        newClasse = ClasseSerializer(data=request.data)
        
        if newClasse.is_valid():
            newClasse.save()

        return Response(newClasse.data, status=status.HTTP_201 )


@api_view(["GET", "POST"])
def categories(request, format=None):

    if request.method=="GET":
        selection = Categorie.objects.all()
        serializer = CategorieSerializer(selection, many=True)

        return Response({ 
            "categories" : serializer.data
        })
    
    if request.method=="POST":
        newCategorie = CategorieSerializer(data=request.data)
        
        if newCategorie.is_valid():
            newCategorie.save()

        return Response(newCategorie.data, status=status.HTTP_201 )

 """

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
    return render(request, "core/pages/index.html")

def aboutPage(request):
    return render(request, "core/pages/about.html")

def solutionsPage(request):
    return render(request, "core/pages/services.html")

def servicePage(request):
    return render(request, "core/pages/service.html")

def ideePage(request):
    return render(request, "core/pages/idee.html")

def projetPage(request):
    return render(request, "core/pages/projet.html")

def contactPage(request):
    return render(request, "core/pages/contact.html")