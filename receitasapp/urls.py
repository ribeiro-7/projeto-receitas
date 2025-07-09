from django.urls import path
from receitasapp import views

app_name = 'receitas'

urlpatterns = [
    path('', views.home, name='home'),
    path('receita/categoria/<int:category_id>/', views.categoria, name='categoria'),
    path('receita/<int:receita_id>/', views.receita, name='receita'),
]