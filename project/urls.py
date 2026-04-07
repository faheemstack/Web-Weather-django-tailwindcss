from django.contrib import admin
from django.urls import path, include
from django.contrib import admin


admin.site.site_header = "Web Weather Admin"       
admin.site.site_title = "Weather Admin"          
admin.site.index_title = "Welcome to the Web Weather " 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
]
