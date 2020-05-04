from nucleo import nucleo
from repositorio.nucleo import microservicio

def servicio(ubicacion, nombre):
	respuesta=nucleo(ubicacion, nombre, microservicio)
	return respuesta  
