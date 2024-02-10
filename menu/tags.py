from django import template
from django.template.loader import render_to_string
from .service import get_dishes_by_category

register = template.Library()

@register.simple_tag
def draw_menu(category_name: str):
    dishes = get_dishes_by_category(category_name) 
    
    return render_to_string('menu_template.html', {
        'dishes': dishes,
    })

