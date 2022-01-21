from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Diet(models.Model):
    date = models.DateField(auto_now_add=True)
    cow_milk = models.BooleanField()
    goat_milk = models.BooleanField()
    apple = models.BooleanField()
    bananna = models.BooleanField()
    egg = models.BooleanField()
    apple_juice = models.BooleanField()
    rice = models.BooleanField()
    teether = models.BooleanField()
    rice_cookie = models.BooleanField()
    puff = models.BooleanField()
    morning_good = models.BooleanField()
    night_good = models.BooleanField()
    chicken = models.BooleanField()
    beef = models.BooleanField()
    pork = models.BooleanField()
    pears = models.BooleanField()
    avocado = models.BooleanField()
    evening_good = models.BooleanField()
    dry_seaweed = models.BooleanField()
    baby_broccoli = models.BooleanField()
    egg_york = models.BooleanField()
    asparagus = models.BooleanField()
    carrot = models.BooleanField()
    red_bean = models.BooleanField()
    seaweed = models.BooleanField()
    tomato = models.BooleanField()
    spinach = models.BooleanField()
    yam = models.BooleanField()
    sea_bass = models.BooleanField()

    def __str__(self):
        return f"{self.date} entry"