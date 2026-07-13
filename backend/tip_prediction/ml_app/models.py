from django.db import models

class TipPrediction(models.Model):
    total_bill = models.FloatField()
    sex = models.CharField(choices=[('Male','Male'),('Female','Female')])
    smoker = models.CharField(choices=[('Yes','Yes'),('No','No')])
    day = models.CharField(choices=[('Thur','Thur'),('Fri','Fri'),('Sat','Sat'),('Sun','Sun')])
    time = models.CharField(choices=[('Lunch','Lunch'),('Dinner','Dinner')])
    