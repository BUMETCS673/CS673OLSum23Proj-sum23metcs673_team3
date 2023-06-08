from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Food, FoodLog

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'
    context_object_name = 'foods'

class FoodLogCreateView(CreateView):
    model = FoodLog
    template_name = 'foodlog_create.html'
    fields = ['user', 'food', 'date']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)