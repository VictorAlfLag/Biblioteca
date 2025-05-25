from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LibrosInicial, LibrosBasica, LibrosBachillerato
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from datetime import datetime


def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')

def listadoLibrosInicial(request):
    libros_inicial = LibrosInicial.objects.all()
    return render(request, "inicial/listado_inicial.html", {'listado_libros_inicial': libros_inicial})

def listadoLibrosBasica(request):
    libros_basica = LibrosBasica.objects.all()
    return render(request, "basica/listado_basica.html", {'listado_libros_basica': libros_basica})

def listadoLibrosBachillerato(request):
    libros_bachillerato = LibrosBachillerato.objects.all()
    return render(request, "bachillerato/listado_bachillerato.html", {'listado_libros_bachillerato': libros_bachillerato})

def nuevoLibroInicial(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        categoria = 'inicial'
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen') 
        documento = request.FILES.get('documento') 
        libro = LibrosInicial(
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion,
            categoria=categoria,
            descripcion=descripcion,
            imagen=imagen,
            documento=documento
        )
        libro.save()
        return redirect('listado_libros')  
    return render(request, 'inicial/nuevo_inicial.html')


def nuevoLibroBasica(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        categoria = 'basica'
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen') 
        documento = request.FILES.get('documento') 
        libro = LibrosBasica(
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion,
            categoria=categoria,
            descripcion=descripcion,
            imagen=imagen,
            documento=documento
        )
        libro.save()
        return redirect('listado_libros')

    return render(request, 'basica/nuevo_basica.html')


def nuevoLibroBachillerato(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        categoria = 'bachillerato'
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')
        documento = request.FILES.get('documento')
        libro = LibrosBachillerato(
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion,
            categoria=categoria,
            descripcion=descripcion,
            imagen=imagen,
            documento=documento
        )
        libro.save()
        return redirect('listado_libros')
    return render(request, 'bachillerato/nuevo_bachillerato.html')

def guardarLibroInicial(request):
    titulo = request.POST['titulo']
    autor = request.POST['autor']
    fecha_publicacion = request.POST['fecha_publicacion']
    imagen = request.FILES.get('imagen')
    categoria = request.POST['categoria']
    descripcion = request.POST['descripcion']
    documento = request.FILES.get('documento')
    
    print(f"Título: {titulo}, Autor: {autor}, Fecha: {fecha_publicacion}, Imagen: {imagen}, Categoria: {categoria}, Descripción: {descripcion}")
    
    libro = LibrosInicial.objects.create(
        titulo=titulo,
        autor=autor,
        fecha_publicacion=fecha_publicacion,
        imagen=imagen,
        categoria=categoria,
        descripcion=descripcion,
        documento=documento
    )
    
    messages.success(request, "Libro registrado exitosamente.")
    return redirect('listado_libros_inicial')


def guardarLibroBasica(request):
    titulo = request.POST['titulo']
    autor = request.POST['autor']
    fecha_publicacion = request.POST['fecha_publicacion']
    imagen = request.FILES.get('imagen')
    categoria = request.POST['categoria']
    descripcion = request.POST['descripcion']
    documento = request.FILES.get('documento')
    
    print(f"Título: {titulo}, Autor: {autor}, Fecha: {fecha_publicacion}, Imagen: {imagen}, Categoria: {categoria}, Descripción: {descripcion}")
    
    libro = LibrosBasica.objects.create(
        titulo=titulo,
        autor=autor,
        fecha_publicacion=fecha_publicacion,
        imagen=imagen,
        categoria=categoria,
        descripcion=descripcion,
        documento=documento
    )
    messages.success(request, "Libro registrado exitosamente.")
    return redirect('listado_libros_basica')


def guardarLibroBachillerato(request):
    titulo = request.POST['titulo']
    autor = request.POST['autor']
    fecha_publicacion = request.POST['fecha_publicacion']
    imagen = request.FILES.get('imagen')
    categoria = request.POST['categoria']
    descripcion = request.POST['descripcion']
    documento = request.FILES.get('documento')
    
    print(f"Título: {titulo}, Autor: {autor}, Fecha: {fecha_publicacion}, Imagen: {imagen}, Categoria: {categoria}, Descripción: {descripcion}")
    
    libro = LibrosBachillerato.objects.create(
        titulo=titulo,
        autor=autor,
        fecha_publicacion=fecha_publicacion,
        imagen=imagen,
        categoria=categoria,
        descripcion=descripcion,
        documento=documento
    )
    messages.success(request, "Libro registrado exitosamente.")
    return redirect('listado_libros_bachillerato')

def editarLibroBachillerato(request, id):
    libro_bachillerato = get_object_or_404(LibrosBachillerato, id_libro=id)
    
    if request.method == 'POST':
        libro_bachillerato.titulo = request.POST.get('titulo')
        libro_bachillerato.autor = request.POST.get('autor')
        fecha_publicacion_str = request.POST.get('fecha_publicacion')
        if fecha_publicacion_str:
            try:
                libro_bachillerato.fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%Y-%m-%d').date()
            except ValueError:
                messages.error(request, "La fecha de publicación no tiene el formato adecuado.")
                return redirect('listado_libros_bachillerato')
        else:
            libro_bachillerato.fecha_publicacion = None
        libro_bachillerato.categoria = request.POST.get('categoria')
        libro_bachillerato.descripcion = request.POST.get('descripcion')
        if 'imagen' in request.FILES:
            libro_bachillerato.imagen = request.FILES['imagen']     
        if 'documento' in request.FILES:
            libro_bachillerato.documento = request.FILES['documento']
        libro_bachillerato.save()
        messages.success(request, "Libro actualizado correctamente.")
        return redirect('listado_libros_bachillerato')
    return render(request, 'bachillerato/editar_bachillerato.html', {'libro': libro_bachillerato})



def editarLibroBasica(request, id):
    libro_basica = get_object_or_404(LibrosBasica, id_libro=id)   
    if request.method == 'POST':
        libro_basica.titulo = request.POST.get('titulo')
        libro_basica.autor = request.POST.get('autor')
        fecha_publicacion_str = request.POST.get('fecha_publicacion')
        if fecha_publicacion_str:
            libro_basica.fecha_publicacion = fecha_publicacion_str  
        libro_basica.categoria = request.POST.get('categoria')
        libro_basica.descripcion = request.POST.get('descripcion')
        if 'imagen' in request.FILES:
            libro_basica.imagen = request.FILES['imagen']
        if 'documento' in request.FILES:
            libro_basica.documento = request.FILES['documento']      
        libro_basica.save()
        return redirect('listado_libros_basica')
    return render(request, 'basica/editar_basica.html', {'libro': libro_basica})

def editarLibroInicial(request, id):
    libro_inicial = get_object_or_404(LibrosInicial, id_libro=id)   
    if request.method == 'POST':
        libro_inicial.titulo = request.POST.get('titulo')
        libro_inicial.autor = request.POST.get('autor')
        fecha_publicacion_str = request.POST.get('fecha_publicacion')
        if fecha_publicacion_str:
            libro_inicial.fecha_publicacion = fecha_publicacion_str
        libro_inicial.categoria = request.POST.get('categoria')
        libro_inicial.descripcion = request.POST.get('descripcion')       
        if 'imagen' in request.FILES:
            libro_inicial.imagen = request.FILES['imagen']       
        if 'documento' in request.FILES:
            libro_inicial.documento = request.FILES['documento']       
        libro_inicial.save()
        return redirect('listado_libros_inicial')  
    return render(request, 'inicial/editar_inicial.html', {'libro': libro_inicial})


def procesoActualizarLibroInicial(request):
    id_libro = request.POST.get('id')
    if not id_libro:
        messages.error(request, "El ID del libro no fue enviado correctamente.")
        return redirect('listado_libros_inicial')
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    fecha_publicacion_str = request.POST.get('fecha_publicacion')
    categoria = request.POST.get('categoria')
    descripcion = request.POST.get('descripcion')
    try:
        if fecha_publicacion_str:
            fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%Y-%m-%d').date()
        else:
            fecha_publicacion = None  
    except ValueError:
        messages.error(request, "La fecha de publicación no tiene el formato adecuado.")
        return redirect('listado_libros_inicial')
    try:
        libro_inicial = LibrosInicial.objects.get(id_libro=id_libro)
    except LibrosInicial.DoesNotExist:
        messages.error(request, "Libro no encontrado.")
        return redirect('listado_libros_inicial')
    libro_inicial.titulo = titulo
    libro_inicial.autor = autor
    libro_inicial.fecha_publicacion = fecha_publicacion
    libro_inicial.categoria = categoria
    libro_inicial.descripcion = descripcion   
    if request.FILES.get('imagen'):
        libro_inicial.imagen = request.FILES.get('imagen')
    if request.FILES.get('documento'):
        libro_inicial.documento = request.FILES.get('documento') 
    libro_inicial.save()
    messages.success(request, "Libro actualizado correctamente.")
    return redirect('listado_libros_inicial')


def procesoActualizarLibroBasica(request):
    id_libro = request.POST.get('id')
    if not id_libro:
        messages.error(request, "El ID del libro no fue enviado correctamente.")
        return redirect('listado_libros_basica')
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    fecha_publicacion_str = request.POST.get('fecha_publicacion')
    categoria = request.POST.get('categoria')
    descripcion = request.POST.get('descripcion')
    try:
        if fecha_publicacion_str:
            fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%Y-%m-%d').date()
        else:
            fecha_publicacion = None  
    except ValueError:
        messages.error(request, "La fecha de publicación no tiene el formato adecuado.")
        return redirect('listado_libros_basica')
    try:
        libro_basica = LibrosBasica.objects.get(id_libro=id_libro)
    except LibrosBasica.DoesNotExist:
        messages.error(request, "Libro no encontrado.")
        return redirect('listado_libros_basica')
    libro_basica.titulo = titulo
    libro_basica.autor = autor
    libro_basica.fecha_publicacion = fecha_publicacion
    libro_basica.categoria = categoria
    libro_basica.descripcion = descripcion
    if request.FILES.get('imagen'):
        libro_basica.imagen = request.FILES.get('imagen')
    if request.FILES.get('documento'):
        libro_basica.documento = request.FILES.get('documento')
    libro_basica.save()
    messages.success(request, "Libro actualizado correctamente.")
    return redirect('listado_libros_basica')

def procesoActualizarLibroBachillerato(request):
    id_libro = request.POST.get('id')
    if not id_libro:
        messages.error(request, "El ID del libro no fue enviado correctamente.")
        return redirect('listado_libros_bachillerato')
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    fecha_publicacion_str = request.POST.get('fecha_publicacion')
    categoria = request.POST.get('categoria')
    descripcion = request.POST.get('descripcion')
    try:
        if fecha_publicacion_str:
            fecha_publicacion = datetime.strptime(fecha_publicacion_str, '%Y-%m-%d').date()
        else:
            fecha_publicacion = None  
    except ValueError:
        messages.error(request, "La fecha de publicación no tiene el formato adecuado.")
        return redirect('listado_libros_bachillerato')
    try:
        libro_bachillerato = LibrosBachillerato.objects.get(id_libro=id_libro)
    except LibrosBachillerato.DoesNotExist:
        messages.error(request, "Libro no encontrado.")
        return redirect('listado_libros_bachillerato')
    libro_bachillerato.titulo = titulo
    libro_bachillerato.autor = autor
    libro_bachillerato.fecha_publicacion = fecha_publicacion
    libro_bachillerato.categoria = categoria
    libro_bachillerato.descripcion = descripcion  
    if 'imagen' in request.FILES:
        libro_bachillerato.imagen = request.FILES['imagen']
    
    if 'documento' in request.FILES:
        libro_bachillerato.documento = request.FILES['documento']  
    libro_bachillerato.save()
    messages.success(request, "Libro actualizado correctamente.")
    return redirect('listado_libros_bachillerato')



def eliminarLibroInicial(request, id):
    libro_inicial = LibrosInicial.objects.get(id_libro=id)
    libro_inicial.delete()
    messages.success(request, "Libro eliminado exitosamente.")
    return redirect('listado_libros_inicial')

def eliminarLibroBasica(request, id):
    libro_basica = LibrosBasica.objects.get(id_libro=id)
    libro_basica.delete()
    messages.success(request, "Libro eliminado exitosamente.")
    return redirect('listado_libros_basica')

def eliminarLibroBachillerato(request, id):
    libro_bachillerato = LibrosBachillerato.objects.get(id_libro=id)
    libro_bachillerato.delete()
    messages.success(request, "Libro eliminado exitosamente.")
    return redirect('listado_libros_bachillerato')

from django.db.models import Q

def verbachillerato(request):
   
    query = request.GET.get('q') 
    libros_bachillerato = LibrosBachillerato.objects.all()
    if query:
        libros_bachillerato = libros_bachillerato.filter(
            Q(titulo__icontains=query) |
            Q(autor__icontains=query)
        )
    return render(request, "visualizaciones/ver_bachillerato.html", {
        'libros_bachillerato': libros_bachillerato, 
        'query': query 
    })

def verbasica(request):
    query = request.GET.get('q')
    libros_basica = LibrosBasica.objects.all()
    if query:
        libros_basica = libros_basica.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
    return render(request, "visualizaciones/ver_basica.html", {
        'libros_basica': libros_basica,
        'query': query
    })

def verinicial(request):
    query = request.GET.get('q')
    libros_inicial = LibrosInicial.objects.all()
    if query:
        libros_inicial = libros_inicial.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
    return render(request, "visualizaciones/ver_inicial.html", {
        'libros_inicial': libros_inicial,
        'query': query
    })

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect('home1') 
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
            return render(request, 'login/registro.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'login/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        print(request.POST)  
        if 'usuario' in request.POST and 'clave' in request.POST:
            username = request.POST['usuario']
            password = request.POST['clave']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home1')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Campos de usuario o contraseña faltantes.')
    return render(request, 'login/login.html')

def ver_estadisticas_libros(request):
    # Contar la cantidad de libros en cada modelo
    conteo_inicial = LibrosInicial.objects.count()
    conteo_basica = LibrosBasica.objects.count()
    conteo_bachillerato = LibrosBachillerato.objects.count()

    # Definir los colores para cada barra del gráfico, manteniendo la coherencia con tus temas
    color_inicial = '#007bff'
    color_basica = '#ff6699'
    color_bachillerato = '#4caf50'

    context = {
        'conteo_inicial': conteo_inicial,
        'conteo_basica': conteo_basica,
        'conteo_bachillerato': conteo_bachillerato,
        'color_inicial': color_inicial,
        'color_basica': color_basica,
        'color_bachillerato': color_bachillerato,
    }
    return render(request, "visualizaciones/estadisticas_libros.html", context)
