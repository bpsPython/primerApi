import json
from flask import Flask, jsonify, request

from puerto import puerto

app = Flask(__name__)

@app.route('/', methods=['Post'])

def entrada():
	print(request.json)
	nombre="nombre" : request.json['nombre']
	ubicacion="ubicacion" : request.json['ubicacion']
	respuesta=puerto.interaccion()
	return jsonify({"respuesta":diccionario})

if __name__ == '__main__':
	app.run(debug=True, port=2553)