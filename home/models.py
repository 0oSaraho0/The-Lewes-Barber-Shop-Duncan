from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    """ A model to list the services the barber shop offers """
    service = models.CharField(max_length=300, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    image = models.ImageField(upload_to='services/')
    time = models.IntegerField(null=False, default=45)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.service)