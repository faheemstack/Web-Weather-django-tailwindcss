from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="Home"),
    path("weather/", views.weather, name="Weather"),
    path("services/", views.services, name="Services"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="Contact"),
]
