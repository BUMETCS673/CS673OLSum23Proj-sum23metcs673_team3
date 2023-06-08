from django.test import TestCase
from foods.models import Food

class FoodModelTestCase(TestCase):
    def test_create_food(self):
        initial_count = Food.objects.count()

        # Create a new food item
        Food.objects.create(name="Apple", calories=52, servings=1, amount_in_grams=100)

        # Check if the count has increased by 1
        self.assertEqual(Food.objects.count(), initial_count + 1)