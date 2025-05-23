from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name="core"

urlpatterns= [
    path("", views.indexHome, name="index"),
    path("about", views.aboutPage, name="about"),
    path("services", views.servicesPage, name="services")
]