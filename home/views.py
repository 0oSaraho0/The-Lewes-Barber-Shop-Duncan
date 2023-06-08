from django.views.generic import TemplateView, ListView, CreateView
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.mixins import LoginRequiredMixin 

# class Index(TemplateView): 
#     template_name = 'home/index.html'

class Services(ListView):
    model = Service
    queryset = Service.objects.order_by('service')
    context_object_name = 'services'
    template_name = 'home/index.html'


class AddService(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'home/add_service.html'
    success_url = 'home/index.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddService, self).form_valid(form)