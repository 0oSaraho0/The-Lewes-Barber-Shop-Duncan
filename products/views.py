from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product


# Create your views here.
class Products(ListView):
    model = Product
    queryset = Product.objects.order_by('product')
    context_object_name = 'products'
    template_name = 'products/products.html'