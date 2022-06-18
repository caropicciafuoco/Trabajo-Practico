from flask import Flask, jsonify, request

from user_loader import load_users
from user_class import Usuario

import requests
from receta_class import Receta


app = Flask(__name__)
users = load_users()


@app.route("/usuarios", methods=['GET'])
def usuarios():  # hay que poner nombres diferentes en las funciones
    return jsonify([user.serialize() for user in users])
    # return jsonify({"Usuarios": users})


@app.route("/info_usuario/<ID>", methods=['GET'])
def usuario_get(ID):  # hay que poner nombres diferentes en las funciones
    for u in users:
        if u.id == ID:
            return jsonify({"Nombre": u.nombre, #se usa el punto para acceder al objeto
                            "Sexo": u.sexo,
                            "Edad": u.edad,
                            "Altura": u.altura,
                            "Peso": u.peso,
                            "Intolerancias": u.restricciones,
                            "Status": "existente"}) #se usa jsonify para transformar diccionarios a json y es necesario porque la API solo trabaja con json

    return jsonify({"ID buscado": ID,
                    "Status": "not found"}) #


@app.route("/crear_usuario", methods=['POST'])
def crear_usario():
    body = request.json #simboliza el body de postman
    nombre = body['nombre']
    contrasena = body['contrasena']
    edad = body['edad']
    sexo = body['sexo']
    peso = body['peso']
    altura = body['altura']
    intolerancia = body['restricciones_alimenticias']

    id = str(int(users[-1].id) + 1) #aca hay que crear la funcion para que cree ID randoms
    #esta funcion sirve para agarrar el ID del usuario anterior y sumarle 1

    nuevo_usuario = Usuario(nombre, contrasena, edad, sexo, peso, altura, intolerancia)
    nuevo_usuario.id = id #le agrego el atributo ID

    users.append(nuevo_usuario) #agrega el objeto a la lista users

    return jsonify({'nuevo_usuario': nuevo_usuario.serialize(), 'status': 'creado'}) #devuelve en la API un diccionario que te muestra al nuevo objeto


@app.route("/eliminar_usuario/<ID>", methods=['DELETE'])
def eliminar_usuario(ID):
    for u in users:
        if u.id == ID:
            users.remove(u)
            return jsonify({'Usuario': u.serialize(),
                            'Status': 'eliminado'})

    return jsonify({'ID buscado': ID,
                    'Status': 'not found'})


@app.route("/cambiar_peso", methods=['PUT'])
def cambiar_peso():
    body = request.json
    ID = body['id']
    nuevo_peso = body['peso']

    for u in users:
        if u.id == ID:
            u.peso = nuevo_peso
            return jsonify({'Usuario' : u.serialize(),
                            'Nuevo Peso' : u.peso,
                            'Status' : 'peso actualizado'})

    return jsonify({'ID buscado': ID,
                    'Status': 'not found'})

@app.route("/cambiar_contrasena", methods=['PUT'])
def cambiar_contrasena():
    body = request.json
    ID = body['id']
    nueva_contrasena = body['contrasena']

    for u in users:
        if u.id == ID:
            u.contrasena = nueva_contrasena
            return jsonify({'Usuario' : u.serialize(),
                            'Nueva Contraseña' : nueva_contrasena,
                            'Status' : 'contraseña actualizada'})

    return jsonify({'ID buscado': ID,
                    'Status': 'not found'})



@app.route("/obtener_receta/<ID>", methods=['GET'])
def obtener_receta(ID):
    url_recetas = 'https://api.spoonacular.com/recipes/complexSearch'
    parametro_intolerancia = ''
    lista_recetas = []
    for u in users:
        if u.id == ID:
            for intolerancia in u.intolerancia:
                if parametro_intolerancia == '':
                    parametro_intolerancia += intolerancia
                else:
                    parametro_intolerancia += ',+' + intolerancia

    http_recetas = (requests.get(url_recetas, params={'apiKey':'bebbf46b8c6c4453b8b051dfca6f3f73', 'intolerance': parametro_intolerancia})).json()

    for r in http_recetas['results']:
        receta = Receta(r['title'], r['id'])
        lista_recetas.append(receta)

    for r in lista_recetas:
        return jsonify({'Receta' : r.title,
                       'Id' : r.id})
