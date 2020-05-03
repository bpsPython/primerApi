import sys
sys.path.append('../')
from repositorio.nucleo import *
sys.path.append('../../')
from ficheros.nucleo import *

class testeo():
	def __init__(self):
		self.nucleo=nucleo()
		self.repo=logicaNucleo()

	def test(self, ubicacion, nombre):
		self.nucleo.microservicio(ubicacion, nombre, self.repo)

#objeto=testeo()
#objeto.test("/home/bps/programas/ddd/Microservicios/", "prueba")