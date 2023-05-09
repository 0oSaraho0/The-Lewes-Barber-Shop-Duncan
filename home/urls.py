from django.urls import path
from .views import Services

urlpatterns =[
    path('', Services.as_view(), name='home'),
    
]