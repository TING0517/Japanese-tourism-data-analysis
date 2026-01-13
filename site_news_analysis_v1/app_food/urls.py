from django.urls import path
from app_food import views

app_name='namespace_food'

urlpatterns = [
    path('', views.home, name='home'),
    path('api_get_food_data/', views.api_get_food_data),
]
