from django.db import models

# Create your models here.


class UserWaterUntake(models.Model):
    water_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

