from django.shortcuts import render

def home(request):
    return render(request, 'receitas/pages/home.html')

def receitas(request, pk):
    return render(
        request, 
        'receitas/pages/receita-view.html'
    )