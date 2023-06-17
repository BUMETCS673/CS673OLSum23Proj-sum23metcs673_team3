from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.index, name="food-journal"),
    path('food-table',views.food_table,name="food-table"),
    path('create-food-item',views.new_food,name="new-food"),
    path('delete-food-item',views.del_food,name="del-food"),
    path('delete-log-entry',views.del_log,name="del-log-entry"),
    path('create-log-entry',views.new_journal_item,name="new-log-entry"),
    path('get-food-names',views.all_food_name,name="get-food-names"),
    path('set-filter',views.update_filter,name="update-filter"),
    path('cal-per-day',views.get_calories_per_day,name="cal-per-day"),
    path('fav-food',views.get_favorite_food,name="fav-food"),
]
