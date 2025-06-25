from django.urls import path
from receitasapp import views

urlpatterns = [
    path('', views.home),
    path('receita/<int:pk>/', views.receita),
]