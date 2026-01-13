from django.urls import path
from app_gpe import views

app_name='namespace_gpe'

urlpatterns = [
    path('', views.home, name='home'),
    path('api_get_gpe_data/', views.api_get_gpe_data),
]
