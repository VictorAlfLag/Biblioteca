from django.db import models

class LibrosInicial(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='inicial/images/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    documento = models.FileField(upload_to='inicial/docs/', blank=True, null=True)

class LibrosBasica(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='basica/images/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    documento = models.FileField(upload_to='basica/docs/', blank=True, null=True)

class LibrosBachillerato(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='bachillerato/images/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    documento = models.FileField(upload_to='bachillerato/docs/', blank=True, null=True)


