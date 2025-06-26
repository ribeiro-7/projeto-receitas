from django.urls import path
from receitasapp import views

app_name = 'receitas'

urlpatterns = [
    path('', views.home, name='home'),
    path('receita/<int:pk>/', views.receita, name='receita'),
]