from django.db import models
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.

class editor(models.Model):
	nombre            = models.CharField(max_length=30)
	direccion         = models.CharField(max_length=50)
	ciudad            = models.CharField(max_length=60)
	estado            = models.CharField(max_length=30)
	pais              = models.CharField(max_length=50)
	sitio_web         = models.URLField()

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ["nombre"]

	class Admin:
		pass

class autor(models.Model):
	saludo        	  = models.CharField(max_length=10)
	primer_nombre     = models.CharField(max_length=30)
	apellido          = models.CharField(max_length=40)
	correo		      = models.EmailField()
	foto	          = models.ImageField(upload_to='libros/')

	def __str__(self):
		return '%s%s' % (self.primer_nombre, self.apellido)

	class Meta:
		ordering = ["primer_nombre"]

	class admin:
		pass


class libros(models.Model):
	titulo            = models.CharField(max_length=100)
	autor             = models.ManyToManyField(autor)
	editor        	  = models.ForeignKey(editor)  
	fecha_publicacion = models.DateField()
	numero_paginas    = models.IntegerField(blank=True)

	
	class Meta:
		ordering = ["titulo"]
	
	class Admin:
		list_display = ('titulo', 'editor', 'fecha_publicacion')
		list_filter = ('editor', 'fecha_publicacion')
		ordering = ('-fecha_publicacion',)
		search_fields = ('titulo',)

	def __str__(self):
		return self.titulo