from django.db import models


# Create your models here.
class User(models.Model):
    user_account = models.CharField(max_length=16, primary_key=True)
    user_name = models.CharField(max_length=32, unique=False, default=user_account)
    user_pwd = models.CharField(max_length=16, default="pwd", blank=False, null=False)
    user_email = models.CharField(max_length=32, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=8, null=True, blank=True)


class Canteen(models.Model):
    canteen_id = models.CharField(max_length=16, primary_key=True)
    canteen_name = models.CharField(max_length=32)
    canteen_location = models.CharField(max_length=64)
    canteen_url = models.URLField()


class Menu(models.Model):
    dish_id = models.CharField(max_length=16, primary_key=True)
    canteen_id = models.ForeignKey(to="Canteen", on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=64, blank=False, null=False, default=dish_id)
    dish_en_name = models.CharField(max_length=64, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    energy = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    carbohydrates = models.IntegerField(null=True, blank=True)
    salt = models.IntegerField(null=True, blank=True)
    calcium = models.IntegerField(null=True, blank=True)
    veg = models.IntegerField(null=True, blank=True)
    iron = models.IntegerField(null=True, blank=True)
    vitaminA = models.IntegerField(null=True, blank=True)
    vitaminB1 = models.IntegerField(null=True, blank=True)
    vitaminB2 = models.IntegerField(null=True, blank=True)
    vitaminC = models.IntegerField(null=True, blank=True)
    place_of_origin = models.CharField(max_length=64, blank=True, null=False, default="Unknown")
    dish_url = models.URLField()

class History_order(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE)
    dish_id = models.ForeignKey(to="Menu", on_delete=models.CASCADE)
    order_date = models.DateField()

