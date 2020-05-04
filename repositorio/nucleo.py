import shlex, subprocess
def microservicio(ubicacion, nombre):
	nivel1='mkdir '
	nivel2=ubicacion + nombre
	nivel3=" " + nivel2 + "/repositorios "
	niveles=nivel1 + nivel2 + nivel3 
	subprocess.call(shlex.split(niveles))

	level1='touch '
	level2=ubicacion + nombre
	level3=" " + level2 + "/__init__.py " + level2 + "/nucleo.py " + level2 + "/servicio.py " + level2 + "/adaptadorEntrada.py " + level2 + "/adaptadorSalida.py "+ level2 + "/puertoEntrada.py "+ level2 + "/puertoSalida.py "
	level4=level2 + "/repositorios/__init__.py " + level2 + "/repositorios/nucleo.py " + level2 + "/repositorios/servicio.py " + level2 + "/repositorios/adaptadorEntrada.py " + level2 + "/repositorios/adaptadorSalida.py " + level2 + "/repositorios/puertoEntrada.py " + level2 + "/repositorios/puertoSalida.py "
	leveles=level1 + level2 + level3 + level4
	subprocess.call(shlex.split(leveles))

	return True