from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models.query_utils import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from foods.models import Food, FoodLog, calculate_food_calories

FILTER = "all"


def index(request):
    current_user = request.user.id
    foods = get_all_journal(current_user)[0]
    calories = get_all_journal(current_user)[1]
    return render(request, 'foods/food_journal.html', {
        "foods": foods,
        "calories": str(calories),
        "applied_filter":FILTER
    })


def food_table(request):
    foods = get_all_foods()
    return render(request, 'foods/food_database.html', {
        "foods": foods,
        "base_dir": settings.BASE_DIR
    })


def get_all_foods():
    response = Food.objects.all()
    food_list = []
    for item in response:
        temp = {
            "name": item.name,
            "calories": item.calories_per_serving,
            "image": item.image
        }
        print(item)
        food_list.append(temp)

    print(food_list)
    return food_list



@api_view(['GET'])
def all_food_name(request):
    food_names = []
    response = Food.objects.all()
    for item in response:
        food_names.append(item.name)
    data = {"food_name": food_names}
    return Response(data, status=200)

@csrf_exempt
@api_view(['POST'])
def update_filter(request):
    global FILTER
    FILTER = request.data.get("filter")
    print(FILTER)
    return Response(status=200)


@api_view(['POST'])
def new_jounal_item(request):
    food = Food.objects.get(name=request.data.get("food_item_name"))
    # print(food.calories_per_serving)
    # print(request.data)
    new_log_entry = FoodLog(user=request.user, food=food, num_of_servings=int(request.data.get("num_servings")))
    new_log_entry.save()
    data = {"user": request.user.id}
    return Response(data, status=200)


# def get_user_journal(time="week"):
#

def get_all_journal(user_id):
    if FILTER == "today":
        enddate = datetime.today()
        startdate = datetime.today() - timedelta(1)
        response = FoodLog.objects.filter(user_id=user_id,time_ate__range=[startdate, enddate])
    elif FILTER == "week":
        enddate = datetime.today()
        startdate = datetime.today()-timedelta(7)
        response = FoodLog.objects.filter(user_id=user_id,time_ate__range=[startdate, enddate])
    elif FILTER == "month":
        enddate = datetime.today()
        startdate = datetime.today()-timedelta(30)
        response = FoodLog.objects.filter(user_id=user_id,time_ate__range=[startdate, enddate])
    else:
        response = FoodLog.objects.filter(user_id=user_id)

    entry_list = []
    total_calories = 0
    for item in response:
        temp = {
            "user": item.user,
            "food_name": item.food.name,
            "calories": item.calories_consumed,
            "num_servings": item.num_of_servings,
            "date": item.time_ate
        }
        total_calories += int(item.calories_consumed)
        print(item)
        entry_list.append(temp)

    print(entry_list)
    return entry_list, total_calories


@api_view(['POST'])
def new_food(request):
    new_food_item = Food(name=request.data.get("food_item_name"), calories_per_serving=request.data.get("calories"))
    new_food_item.save()
    data = {"name": new_food_item.name}
    return Response(data, status=200)
