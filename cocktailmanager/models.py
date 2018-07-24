from django.db import models
from django.contrib.auth.models import User


class Calorie(models.Model):
    name = models.CharField(max_length=250)
    calories = models.IntegerField(default=0)
    fat = models.CharField(max_length=250)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    sugar = models.IntegerField(default=0)


class Alcohol(models.Model):
    name = models.CharField(max_length=250)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    image = models.ImageField(upload_to='alcohol')
    icon = models.CharField(max_length=250)
    alcohol_rate = models.IntegerField(default=0)


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ingredient')


class Glass(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ingredient')


class Cocktail(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=False)
    name = models.CharField(max_length=250)
    glass = models.ForeignKey(Glass, on_delete=models.CASCADE)
    method = models.CharField(max_length=200)
    difficulty = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cocktail')
    price = models.CharField(max_length=200)
    recipe = models.CharField(max_length=1000)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    # rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    calories = models.ForeignKey(Calorie, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
