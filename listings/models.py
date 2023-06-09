from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='')
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)

    def get_photos(self):
        return self.d

    def __str__(self):
        return self.title

