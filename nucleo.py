from repositorio.nucleo import microservicio
def nucleo(ubicacion, nombre):
	respuesta=microservicio(ubicacion, nombre)
	return respuesta