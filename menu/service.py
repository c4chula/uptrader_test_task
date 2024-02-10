from django.db.models import QuerySet
from .models import Dish, Category 

def get_all_categories() -> QuerySet[Category]:
    return Category.objects.all()

def get_first_category() -> Category:
    return Category.objects.first()

def get_dishes_by_category(category_name: str) -> QuerySet[Dish]:
    print(category_name)
    return Category.objects.filter(name=category_name).first().dish_set.all()
