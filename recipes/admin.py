from django.contrib import admin
from .models import Recipe, Ingredient, Food, VegetarianFood, MeasureTable

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(VegetarianFood)
admin.site.register(MeasureTable)
