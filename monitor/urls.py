from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/stats/', views.system_stats_api, name='system_stats_api'), # Live API route
    path('health-check/', views.health_check_view, name='health_check'),
]