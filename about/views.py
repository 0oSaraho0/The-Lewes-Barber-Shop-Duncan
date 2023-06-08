from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import About


class About(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'about/about.html'