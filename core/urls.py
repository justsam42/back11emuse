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

    path("api/index", views.api_index, name="api_index"),
    path("api/test", views.api_test, name="api_test"),
    path("api/<str:name>", views.objet, name="objet"),

    path("api/texts", views.text, name="texts")
]

urlpatterns = format_suffix_patterns(urlpatterns)


