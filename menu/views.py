from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .service import get_all_categories, get_dishes_by_category, get_first_category

def show_first_menu_category(request: HttpRequest) -> HttpResponse:
    current_category = get_first_category()
    if not current_category:
        return render(request, 'menu/empty.html', {})
    return HttpResponseRedirect(redirect_to=f"{current_category.name}")

def show_menu_for_category(request: HttpRequest, category_name: str) -> HttpResponse:
    categories = get_all_categories()
    current_category = categories.filter(name=category_name).first()

    return render(request, 'menu/home.html', {
        'current_category': current_category.name, 
        'categories': categories,
    })
