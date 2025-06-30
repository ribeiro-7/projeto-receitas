from django.shortcuts import render
from utils.receitas.factory import make_recipe
from django.shortcuts import get_list_or_404
from .models import Receita

def home(request):

    receitas = Receita.objects.all().filter(is_published=True).order_by('-id')

    return render(
        request, 
        'receitas/pages/home.html',
        context={
            'receitas': receitas,
        }
    )

def receita(request, pk):
    return render(
        request, 
        'receitas/pages/receita-view.html',
        context={
            'receita': make_recipe(),
            'is_detail_page': True,
        }
    )

def categoria(request, category_pk):

    #receitas = Receita.objects.all().filter(category__id = category_pk, is_published=True).order_by('-id')

    receitas = get_list_or_404(
        Receita.objects.all().filter(category__id = category_pk, is_published=True).order_by('-id')
    )

    return render(
        request,
        'receitas/pages/category.html',
        context={
            'receitas': receitas,
            'title': f'{receitas[0].category.name} - Category | '
        }
    )