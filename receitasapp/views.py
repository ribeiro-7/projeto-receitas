from django.shortcuts import render
from utils.receitas.factory import make_recipe
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Receita

def home(request):

    receitas = Receita.objects.filter(is_published=True).order_by('-id')

    return render(
        request, 
        'receitas/pages/home.html',
        context={
            'receitas': receitas,
        }
    )

def receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id, is_published=True)

    return render(
        request, 
        'receitas/pages/receita-view.html',
        context={
            'receita': receita,
            'is_detail_page': True,
            'title': f'{receita.title} - '
        }
    )

def categoria(request, category_id):

    #receitas = Receita.objects.all().filter(category__id = category_pk, is_published=True).order_by('-id')

    receitas = get_list_or_404(
        Receita.objects.all().filter(category__id = category_id, is_published=True).order_by('-id')
    )

    return render(
        request,
        'receitas/pages/category.html',
        context={
            'receitas': receitas,
            'title': f'{receitas[0].category.name} - Category | '
        }
    )