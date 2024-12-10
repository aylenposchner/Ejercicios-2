from django.shortcuts import render
from . import models, forms

def index(request):
    return render(request,"producto/index.html")

def Categoria_list(request):
    categorias = models.Categoria.objects.all()
    return render(request,"producto/categoria_list.html",{"categorias":categorias})

def Categoria_create(request):
    form = forms.CategoriaForm()
    return render(request,"producto/categoria_form.html",{"form":form})