from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.index, name="food-journal"),
    path('food-table',views.food_table,name="food-table"),
    path('create-food-item',views.new_food,name="new-food"),
    path('create-log-entry',views.new_jounal_item,name="new-log-entry"),
    path('get-food-names',views.all_food_name,name="get-food-names"),
    path('set-filter',views.update_filter,name="update-filter")

]
