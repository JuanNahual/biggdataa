from django.shortcuts import render
from .models import Empresa
from django.shortcuts import render, get_object_or_404

def lista_empresas(request):
    query = request.GET.get('q')
    rubro = request.GET.get('rubro')
    empresas = Empresa.objects.all()

    if query:
        empresas = empresas.filter(nombre__icontains=query)
    if rubro:
        empresas = empresas.filter(rubro=rubro)

    rubros = Empresa.objects.values_list('rubro', flat=True).distinct()
    return render(request, 'Empresas/lista_empresas.html', {'empresas': empresas, 'rubros': rubros})



def detalle_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    return render(request, 'Empresas/detalle_empresa.html', {'empresa': empresa})


def home(request):
    return render(request, 'Empresas/home.html')
