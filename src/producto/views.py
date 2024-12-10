from django.shortcuts import render, redirect
from . import models, forms

def index(request):
    return render(request,"producto/index.html")

def Categoria_list(request):
    categorias = models.Categoria.objects.all()
    return render(request,"producto/categoria_list.html",{"categorias":categorias})

def Categoria_create(request):
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")

    return render(request,"producto/categoria_form.html",{"form":form})