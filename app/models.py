from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipeID  = models.CharField(max_length=200)
    name = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name


class FoodItems(models.Model):
    itemID  = models.TextField()
    name = models.CharField(max_length=200)
    category = models.TextField()
    expiryDate = models.TextField()

    def __str__(self):
        return self.name


class FoodWaste(models.Model):
    wasteID  = models.CharField(max_length=200)
    itemID  = models.CharField(max_length=200)
    quantityWasted = models.TextField()
    reason = models.TextField()
    items = models.ManyToManyField(FoodItems, related_name='unused_field')

    def __str__(self):
        return self.wasteID