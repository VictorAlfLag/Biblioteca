from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_view, name='login'),
    path('home1/', views.home1, name='home1'),
    # Rutas para Libros Inicial
    path('listadoLibrosInicial/', views.listadoLibrosInicial, name='listado_libros_inicial'),
    path('eliminarLibroInicial/<id>', views.eliminarLibroInicial, name='eliminarLibroInicial'),
    path('editarLibroInicial/<int:id>/', views.editarLibroInicial, name='editarLibroInicial'),
    path('guardarLibroInicial/', views.guardarLibroInicial, name='guardarLibroInicial'),
    path('procesoActualizarLibroInicial/', views.procesoActualizarLibroInicial, name='procesoActualizarLibroInicial'),
    path('nuevoLibroInicial/', views.nuevoLibroInicial, name='nuevoLibroInicial'),

    
    # Rutas para Libros Básica
    path('listadoLibrosBasica/', views.listadoLibrosBasica, name='listado_libros_basica'),
    path('eliminarLibroBasica/<id>', views.eliminarLibroBasica, name='eliminarLibroBasica'),
    path('editarLibroBasica/<int:id>/', views.editarLibroBasica, name='editarLibroBasica'),
    path('guardarLibroBasica/', views.guardarLibroBasica, name='guardarLibroBasica'),
    path('procesoActualizarLibroBasica/', views.procesoActualizarLibroBasica, name='procesoActualizarLibroBasica'),
    path('nuevoLibroBasica/', views.nuevoLibroBasica, name='nuevoLibroBasica'),
    
    # Rutas para Libros Bachillerato
    path('listadoLibrosBachillerato/', views.listadoLibrosBachillerato, name='listado_libros_bachillerato'),
    path('eliminarLibroBachillerato/<id>', views.eliminarLibroBachillerato, name='eliminarLibroBachillerato'),
    path('editarLibroBachillerato/<int:id>/', views.editarLibroBachillerato, name='editarLibroBachillerato'),
    path('guardarLibroBachillerato/', views.guardarLibroBachillerato, name='guardarLibroBachillerato'),
    path('procesoActualizarLibroBachillerato/', views.procesoActualizarLibroBachillerato, name='procesoActualizarLibroBachillerato'),
    path('nuevoLibroBachillerato/', views.nuevoLibroBachillerato, name='nuevoLibroBachillerato'),

     # Rtas para verinicial, verbasica, verbachillerato, 
    path('verbachillerato/', views.verbachillerato, name='ver_libros_bachillerato'),
    path('verinicial/', views.verinicial, name='ver_libros_inicial'),
    path('verbasica/', views.verbasica, name='ver_libros_basica'),
    path('estadisticas-libros/', views.ver_estadisticas_libros, name='estadisticas_libros'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)