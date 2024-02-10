from django.contrib import admin
from django.contrib.admin.options import RedirectView
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("menu.urls")),
    path("", RedirectView.as_view(url="menu")),
]
