from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


handler404 = "core.views.page_not_found"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="Home"),
    path("weather/", views.weather, name="Weather"),
    path("services/", views.services, name="Services"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="Contact"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
     path('logout/', views.logout_view, name="logout"),
    # path("profile/", views.profile_view, name="profile"),
    path("profile/<str:email>/", views.profile, name="profile"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)