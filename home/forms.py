from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Service

class ServiceForm(forms.ModelForm):
    """ A form to create a service """

    class Meta:
        model = Service
        fields = ['service', 'price', 'image', 'time', 'description',]

        labels = {
            'service': 'Service Name',
            'price': 'Price',
            'image': 'Image',
            'time': 'Time taken',
            'description': 'Service Description'
        }