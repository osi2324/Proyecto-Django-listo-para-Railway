from django.urls import path
from . import views
from .views import generar_reporte_pdf


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipos/nuevo/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    

  # Página del chatbot
    path('chatbot/', views.chatbot_view, name='chatbot'),

    # API que responde
    path('chatbot-api/', views.chatbot, name='chatbot_api'),

path("reporte/pdf/", generar_reporte_pdf, name="reporte_pdf"),
    

]
