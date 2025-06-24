from django.urls import path
from receitasapp import views

urlpatterns = [
    path('', views.home),
    path('receitas/<int:pk>/', views.receitas),
]