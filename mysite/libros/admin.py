from django.contrib import admin
from libros.models import editor, autor, libros

admin.site.register(autor)
admin.site.register(editor)
admin.site.register(libros)