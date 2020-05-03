import sys
sys.path.append('../../')
from ficheros.puerto import *

class testeo():
	def __init__(self):
		self.puerto=puerto()

	def test(self, diccionario):
		var=self.puerto.interaccion(diccionario)		
		return var
#objeto=testeo()
#diccionario={"ubicacion":"/home/bps/programas/ddd/Microservicios/", "nombre":"prueba"}
#var=objeto.test(diccionario)
#print("El objeto retornado es: " + str(var))