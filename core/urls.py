from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name="core"

urlpatterns= [
    path("", views.indexHome, name="index"),
    path("presentation-muse", views.aboutPage, name="presentation"),
    path("solutions", views.solutionsPage, name="solutions"),
    path("service-sur-mesure", views.servicePage, name="service"),
    path("avoir-une-idee", views.ideePage, name="idee"),
    path("accompagnement-projet", views.projetPage, name="projet"),
    path("contact", views.contactPage, name="contact"),
]