from nucleo import *
from repositorio.nucleo import *

class servicio:
	def __init__(self):
		self.nucleo=nucleo()
		self.dependencia=logicaNucleo()
		self.respuesta=[]

	def caso_uso(self, ubicacion, nombre):
		var=self.nucleo.microservicio(ubicacion, nombre, self.dependencia)
		self.respuesta.append(ubicacion)
		self.respuesta.append(nombre)
		return var  