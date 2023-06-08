from django.contrib import admin

# Register your models here.
from .models import Food, FoodLog

admin.site.register(Food)
admin.site.register(FoodLog)