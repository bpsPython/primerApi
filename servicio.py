from nucleo import *
from repositorio.nucleo import *

class servicio:
	def __init__(self):
		self.nucleo=nucleo()
		self.dependencia=logicaNucleo()

	def caso_uso(self, ubicacion, nombre):
		respuesta=self.nucleo.microservicio(ubicacion, nombre, self.dependencia)
		return respuesta  