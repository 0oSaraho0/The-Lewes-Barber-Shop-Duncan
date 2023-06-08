from django.db import models

from djrichtextfield.models import RichTextField

class About(models.Model):
    about = RichTextField(max_length=10000, null=False, blank=False)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return str(self.about)
    

class Artist(models.Model):
    artist = models.CharField(max_length=500)
    website = models.URLField(max_length=200, blank=True)
    date_entered = models.DateTimeField(auto_now=True)
    about = models.CharField(max_length=5000, null=True)
    image = models.ImageField(upload_to='artist/', null=True)

    def __str__(self):
        return str(self.artist)


# Create your models here.
