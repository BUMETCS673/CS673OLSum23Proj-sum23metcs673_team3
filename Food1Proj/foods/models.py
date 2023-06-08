# Foods - Adithya
from django.db import models
from django.contrib.auth.models import User
from calorieCalculation.utils import calculate_food_calories
from django.utils import timezone

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories_per_serving = models.IntegerField()
    image = models.ImageField(upload_to='food_images', default='/home/adi/Pictures/Mahavatar-Babaji-Maharaj.jpg')

    def __str__(self):
        return self.name


class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    num_of_servings = models.IntegerField()
    time_ate = models.DateTimeField(default=timezone.now)
    calories_consumed = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.food.name} ({self.time_ate})"
    
    '''
    def save(self, *args, **kwargs):
        # Calculate the calories consumed using the calculate_food_calories function
        self.calories_consumed = calculate_food_calories(self.food.calories, self.food.servings, self.food.amount_in_grams)
        super().save(*args, **kwargs)
    '''

    def save(self, *args, **kwargs):
        if self.food.calories_per_serving is None or self.num_of_servings is None:
            raise ValueError("Invalid food information provided.")
        
        self.calories_consumed = calculate_food_calories(self.food.calories_per_serving, self.num_of_servings) 
        super().save(*args, **kwargs)
