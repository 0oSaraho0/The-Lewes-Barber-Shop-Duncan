from django.urls import path
from .views import Services, AddService

urlpatterns =[
    path('', Services.as_view(), name='home'),
    path('add/', AddService.as_view(), name='add_service')
    
]