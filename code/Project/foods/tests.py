from django.test import TestCase
from django.contrib.auth.models import User
from .models import Food, FoodLog, calculate_food_calories

class FoodModelTestCase(TestCase):
    def test_food_model_str_representation(self):
        food = Food.objects.create(name='Pizza', calories_per_serving=250)
        self.assertEqual(str(food), 'Pizza')

    def test_food_log_model_calories_consumed(self):
        user = User.objects.create(username='testuser')
        food = Food.objects.create(name='Burger', calories_per_serving=300)
        food_log = FoodLog.objects.create(user=user, food=food, num_of_servings=2)
        self.assertEqual(food_log.calories_consumed, 600)


    def test_food_log_model_save_method(self):
        user = User.objects.create(username='testuser')
        food = Food.objects.create(name='Salad', calories_per_serving=150)
        food_log = FoodLog(user=user, food=food, num_of_servings=1)
        food_log.save()
        self.assertIsNotNone(food_log.calories_consumed)


class CalculateFoodCaloriesTestCase(TestCase):
    def test_calculate_food_calories(self):
        base_calories = 100
        servings = 2
        expected_calories = 200
        food = FoodLog()
        calculated_calories = calculate_food_calories(base_calories, servings)
        self.assertEqual(calculated_calories, expected_calories)

#These tests cover different scenarios such as checking the string 
# representation of the Food model, calculating calories consumed 
# in the FoodLog model, handling invalid food information in the 
# FoodLog model, and testing the calculate_food_calories function.






