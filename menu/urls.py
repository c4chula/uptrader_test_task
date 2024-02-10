from django.urls import path

from . import views

urlpatterns = [
    path("menu/", views.show_first_menu_category),
    path("menu/<str:category_name>", views.show_menu_for_category, name="menu"),
]
