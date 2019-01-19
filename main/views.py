from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from lugares.models import Lugar
from usuarios.models import Usuario
from lugares.models import Departamento


def home(request):
    return render(request,'home.html')

def buscarView(request):
    busqueda = request.GET.get('busqueda')
    context = {'busqueda': busqueda}

    if busqueda is '':
        context['mensaje'] = 'No se ha ingresado nada para buscar'
    else:
        lugares = Lugar.objects.filter(nombre__icontains = busqueda)
        lugares = [lugar_to_dict(lugar) for lugar in lugares]
        context['lugares'] = lugares

    return render(request, 'buscar.html',context)


# Serializa un Lugar a un objeto tipo Json para agregarlo en extra_context
def lugar_to_dict(lugar):
    if lugar is not None:
        return {'id_lugar':lugar.id_lugar,
                'nombre':lugar.nombre,
                'descripcion':lugar.descripcion,
                'capacidad':lugar.capacidad,
                'img_ppal':lugar.img_ppal,
                'ciudad_id':lugar.ciudad_id
                }
    else:
        return None
