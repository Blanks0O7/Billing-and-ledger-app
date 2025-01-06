from django.urls import path
from . import views

urlpatterns = [
    path('stock/', views.stock_overview, name='stock_overview'),
]