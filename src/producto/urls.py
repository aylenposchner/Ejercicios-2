from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path("",views.index, name="index"),
    path("categoria/list/",views.Categoria_list, name="categoria_list"),
    path("categoria/create/",views.Categoria_create, name="categoria_form"),
]
