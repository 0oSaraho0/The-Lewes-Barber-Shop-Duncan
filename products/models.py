from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    """ a model to list the barber shop products for sale"""
    product = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='products/', force_format='WEBP',
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.product)





