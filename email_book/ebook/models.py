from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
     return str(self.id)