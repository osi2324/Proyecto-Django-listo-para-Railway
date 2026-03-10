from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo
from .ia import detectar_anomalias
from django.http import JsonResponse, HttpResponse
from .forms import EquipoForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from datetime import datetime


def dashboard(request):
    equipos = Equipo.objects.all()

    total = equipos.count()
    activos = equipos.filter(estado="activo").count()
    reparacion = equipos.filter(estado="reparacion").count()
    baja = equipos.filter(estado="baja").count()

    anomalias = detectar_anomalias()

    return render(request, 'inventario/dashboard.html', {
        'equipos': equipos,
        'total': total,
        'activos': activos,
        'reparacion': reparacion,
        'baja': baja,
        'anomalias': anomalias
    })


def chatbot(request):

    mensaje = request.GET.get('msg','').lower()

    total = Equipo.objects.count()
    activos = Equipo.objects.filter(estado='activo').count()
    reparacion = Equipo.objects.filter(estado='reparacion').count()
    baja = Equipo.objects.filter(estado='baja').count()

    if "total" in mensaje:
        respuesta = f"Hay {total} equipos registrados"

    elif "activo" in mensaje:
        respuesta = f"Hay {activos} equipos activos"

    elif "reparacion" in mensaje:
        respuesta = f"Hay {reparacion} en reparación"

    elif "baja" in mensaje:
        respuesta = f"Hay {baja} dados de baja"

    elif "anomalia" in mensaje:
        respuesta = str(detectar_anomalias())

    elif "hola" in mensaje:
        respuesta = "Hola 👋 Soy el asistente inteligente de inventario"

    else:
        respuesta = "No entendí la pregunta 🤔"
    

    return JsonResponse({'reply': respuesta})
def chatbot_view(request):
    return render(request, "inventario/chatbot.html")


# LISTAR
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'inventario/lista.html', {'equipos': equipos})


# CREAR
def crear_equipo(request):
    form = EquipoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_equipos')
    return render(request, 'inventario/form.html', {'form': form})


# EDITAR
def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    form = EquipoForm(request.POST or None, instance=equipo)
    if form.is_valid():
        form.save()
        return redirect('lista_equipos')
    return render(request, 'inventario/form.html', {'form': form})


# ELIMINAR
def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('lista_equipos')

    from django.shortcuts import render

def sobre_nosotros(request):
    return render(request, 'inventario/sobre_nosotros.html')


# PDFFFFFFF


def generar_reporte_pdf(request):
    equipos = Equipo.objects.all()

    template = get_template("inventario/reporte_pdf.html")
    html = template.render({
        "equipos": equipos,
        "fecha_actual": datetime.now()
    })

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_inventario.pdf"'

    pisa_status = pisa.CreatePDF(
        html,
        dest=response
    )

    if pisa_status.err:
        return HttpResponse("Error al generar PDF", status=500)

    return response