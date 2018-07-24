from django.db import models
from django.contrib.auth.models import User


class Calorie(models.Model):
    name = models.CharField(max_length=250)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    image = models.ImageField(upload_to='alcohol')


class Alcohol(models.Model):
    name = models.CharField(max_length=250)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    image = models.ImageField(upload_to='alcohol')
    alcohol_rate = models.IntegerField(default=0)


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    image = models.ImageField(upload_to='alcohol')


class Cocktail(models.Model):
    # ingredients = models.ForeignKey("Ingredient", on_delete=False)
    name = models.CharField(max_length=250)
    glass = models.CharField(max_length=200)
    method = models.CharField(max_length=200)
    difficulty = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cocktail')
    price = models.CharField(max_length=200)
    recipe = models.CharField(max_length=1000)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True, auto_now_add=True)
