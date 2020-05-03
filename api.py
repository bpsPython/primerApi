from flask import Flask, jsonify, request
from puerto import puerto

app = Flask(__name__)

@app.route('/', methods=['Post'])

def entrada():
	#print(request.json)

	diccionario = {
		"nombre" : request.json['nombre'],
		"ubicacion" : request.json['ubicacion']
	}
	
	respuesta=puerto.interaccion(diccionario)

	if respuesta==True:
		return jsonify({"respuesta":"200"})
	return jsonify({"respuesta":"400"})

if __name__ == '__main__':
	app.run(debug=True, port=2553)