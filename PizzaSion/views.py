from django.http import HttpResponse
from django.shortcuts import render
from PizzaSion.models import Pizzas
from PizzaSion.forms import PizzaFormulario

# Create your views here.

def pizzas(self):

    pizza =  Pizzas(nombre="Especial", tamanio="Familiar", ingredientes= "Jamon , Morron, Ajo y albahaca", precio= 1300)
    pizza.save()
    documento = f"Pizza: {pizza.nombre}, Tamaño: {pizza.tamanio}, Ingredientes: {pizza.ingredientes}, Precio:{pizza.precio}"

    return HttpResponse(documento)

def inicio(request):
    pizzasion = Pizzas.objects.all()
    contexto= {'pizzas':pizzasion}   
    return render(request,"PizzaSion/inicio.html",contexto)

def pizzas(request):

    pizzasion = Pizzas.objects.all()
    contexto= {'pizzas':pizzasion}

    return render(request,"PizzaSion/pizzas.html", contexto)        

def crearPizza(request):

   if request.method == "POST":

        miFormulario = PizzaFormulario(request.POST)

        print(miFormulario)

        if PizzaFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           pizza = Pizzas (nombre=informacion['nombre'],foto=informacion['foto'], tamanio=informacion['tamanio'], ingredientes=informacion['ingredientes'], precio=informacion['precio'])

           pizza.save()

           return render(request, "PizzaSion/inicio.html")    

   else:

      miFormulario= PizzaFormulario()

   return render(request,'PizzaSion/formulario.html',{"miFormulario":miFormulario})    

def buscarPizza(request):

    return render(request, "PizzaSion/buscarPizza.html")

def buscar(request):

    if request.GET['nombre']:
       nombre = request.GET['nombre']
       pizzas = Pizzas.objects.filter(nombre__icontains=nombre)

       return render(request,"PizzaSion/resultadosBusqueda.html",{"pizzas": pizzas,"nombre":nombre})

    else:
      
      respuesta = "No enviaste datos"

    return HttpResponse(respuesta)