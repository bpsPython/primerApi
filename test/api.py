import sys
sys.path.append('../../')
from ficheros.api import *

class testeo():
	def __init__(self):
		self.api=api()

	def test(self, archivoJson):
		var=self.api.application(archivoJson)		
		return var

objeto=testeo()
var=objeto.test("/home/bps/programas/ddd/Microservicios/ficheros/archivo.json")
print("El resultado es:" + str(var))
