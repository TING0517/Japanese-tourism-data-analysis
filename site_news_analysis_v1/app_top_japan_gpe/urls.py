from django.urls import path
from app_top_japan_gpe import views

app_name="app_top_japan_gpe"

urlpatterns = [
    path('', views.home, name='home'),
    path('api_get_topgpe/', views.api_get_topgpe, name='api_get_topgpe'),
]
