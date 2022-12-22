from django.shortcuts import render 

from producto.models import Producto

def inicio(request):
    template_name = "index.html"


    #--------------------------------------------------
    #query en django utilizando orm
    """
    p = Producto.objects.create(
    nombre = "pantalon",
    precio = "2000",
    descripcion = "pantalon azul",
    )
    """
    productos = Producto.objects.all()
    print(productos)
    contexto = {
        "productos": productos
    }
    return render(request, template_name, contexto)