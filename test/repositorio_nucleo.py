import sys
sys.path.append('../')
from repositorio.nucleo import *

class testeo():
	def __init__(self):
		self.repo=logicaNucleo()
		
	def test(self, ubicacion, nombre):
		self.repo.microservicio(ubicacion, nombre)

#objeto=testeo()
#objeto.test("/home/bps/programas/ddd/Microservicios/", "prueba")