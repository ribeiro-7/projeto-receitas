from django.contrib import admin
from .models import Category, Receita

class CategoryAdmin(admin.ModelAdmin):
    ...

class ReceitaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Receita, ReceitaAdmin)