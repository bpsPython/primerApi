from servicio import *
class puerto:
	def __init__(self):
		self.servicio=servicio()

	def interaccion(self, diccionario):
		ubicacion=diccionario["ubicacion"]
		nombre=diccionario["nombre"]
		var=self.servicio.caso_uso(ubicacion, nombre)
		return var