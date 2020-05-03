import sys
sys.path.append('../../')
from ficheros.servicio import *

class testeo():
	def __init__(self):
		self.servicio=servicio()
		
	def test(self, ubicacion, nombre):
		self.servicio.caso_uso(ubicacion, nombre)

#objeto=testeo()
#objeto.test("/home/bps/programas/ddd/Microservicios/", "prueba")