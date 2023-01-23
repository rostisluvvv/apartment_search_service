from django.db import models


class ApartmentInfo(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    apartment_area = models.FloatField(max_length=30)
    price = models.FloatField(max_length=30)
    contact = models.IntegerField(max_length=20)

