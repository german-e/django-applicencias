from django.urls import path, include
from django.views.generic import CreateView

urlpatterns = [    
    path('register/', CreateView.as_view(template_name='registration/register') , name='register'),
]