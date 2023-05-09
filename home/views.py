from django.views.generic import TemplateView, ListView
from .models import Service

# class Index(TemplateView):
#     template_name = 'home/index.html'

class Services(ListView):
    model = Service
    queryset = Service.objects.order_by('service')
    context_object_name = 'services'
    template_name = 'home/index.html'