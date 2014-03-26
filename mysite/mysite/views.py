# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

artMusicos = [
    {'nombre': 'Django Reinhardt', 'genero': 'jazz'},
    {'nombre': 'Jimi Hendrix',     'genero': 'rock'},
    {'nombre': 'Louis Armstrong',  'genero': 'jazz'},
    {'nombre': 'Pete Townsend',    'genero': 'rock'},
    {'nombre': 'Yanni',            'genero': 'new age'},
    {'nombre': 'Ella Fitzgerald',  'genero': 'jazz'},
    {'nombre': 'Wesley Willis',    'genero': 'casio'},
    {'nombre': 'John Lennon',      'genero': 'rock'},
    {'nombre': 'Bono',             'genero': 'rock'},
    {'nombre': 'Garth Brooks',     'genero': 'country'},
    {'nombre': 'Duke Ellington',   'genero': 'jazz'},
    {'nombre': 'William Shatner',  'genero': 'spoken word'},
    {'nombre': 'Madonna',          'genero': 'pop'},
]

import datetime
def horaActual(request):
	fecha = datetime.datetime.now()
	return render_to_response('hora.html', {'horaActual': fecha })

def horas(request, offset):
	offset = int(offset) #CADENA DE CARACTERES QUE SE CAPTURA EN LOS PARENTESIS EN PATRON URL
	horaFuturas = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('horaFuturas.html', { 'cantidadHoras' : offset , 'horas': horaFuturas })

#def musicos(request):
#	return render_to_response('musicos/musicosGeneros.html', {'musicosGeneros':musicosGeneros})

def listamusicos(request):
	musicosGeneros = []
    	for musicGerero in artMusicos:
    		musicosGeneros.append({
    			'nombre': musicGerero['nombre'],
    			'genero': musicGerero['genero'],
    			'importante': musicGerero['genero'] in ('rock', 'jazz')
    		})
	return render_to_response('musicos/listaMusicosGeneros.html', {'musicosGeneros':musicosGeneros})