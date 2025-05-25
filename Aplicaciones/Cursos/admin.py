from django.contrib import admin

from .models import LibrosInicial, LibrosBasica, LibrosBachillerato

# Registra los modelos en el administrador
admin.site.register(LibrosInicial)
admin.site.register(LibrosBasica)
admin.site.register(LibrosBachillerato)