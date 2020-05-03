import shlex, subprocess
class logicaNucleo():
	def __init__(self):
		self.nombre=""
		self.ubicacion=""
		self.instrucciones=[]

	def niveles(self):
		nivel1='mkdir '
		nivel2=self.ubicacion + self.nombre
		nivel3=" " + nivel2 + "/repositorios "
		niveles=nivel1 + nivel2 + nivel3 
		return niveles
	
	def directorios(self):
		niveles=self.niveles()
		subprocess.call(shlex.split(niveles))

	def modulos(self):
		nivel1='touch '
		nivel2=self.ubicacion + self.nombre
		nivel3=" " + nivel2 + "/__init__.py " + nivel2 + "/nucleo.py " + nivel2 + "/servicio.py " + nivel2 + "/adaptadorEntrada.py " + nivel2 + "/adaptadorSalida.py "+ nivel2 + "/puertoEntrada.py "+ nivel2 + "/puertoSalida.py "
		nivel4=nivel2 + "/repositorios/__init__.py " + nivel2 + "/repositorios/nucleo.py " + nivel2 + "/repositorios/servicio.py " + nivel2 + "/repositorios/adaptadorEntrada.py " + nivel2 + "/repositorios/adaptadorSalida.py " + nivel2 + "/repositorios/puertoEntrada.py " + nivel2 + "/repositorios/puertoSalida.py "
		niveles=nivel1 + nivel2 + nivel3 + nivel4
		return niveles

	def archivos(self):
		niveles=self.modulos()
		subprocess.call(shlex.split(niveles))

	def microservicio(self, ubicacion, nombre):
		if nombre == "":
			print("error, ingrese texto")
		else:
			self.ubicacion=ubicacion
			self.nombre=nombre
			self.directorios()
			self.archivos()
			return True