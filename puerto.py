from servicio import servicio
def puerto(diccionario):
	ubicacion=diccionario["ubicacion"]
	nombre=diccionario["nombre"]
	respuesta=servicio(ubicacion, nombre)
	return respuesta
