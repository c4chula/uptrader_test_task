from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "categories"

    def __str__(self) -> str:
        return f"{self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Dishes"
        db_table = "dishes"

    def __str__(self) -> str:
        return f"{self.name}"
