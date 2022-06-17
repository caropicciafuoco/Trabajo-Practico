from flask import Flask, jsonify, request

from user_loader import load_users
from usuario import Usuario

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
                            "Restriccion Alimenticias": u.restricciones,
                            "status": "existente"}) #se usa jsonify para transformar diccionarios a json y es necesario porque la API solo trabaja con json

    return jsonify({"ID buscado": ID,
                    "status": "not found"}) #


@app.route("/crear_usuario", methods=['POST'])
def crear_usario():
    body = request.json #simboliza el body de postman
    nombre = body['nombre'] #
    contrasena = body['contrasena']
    edad = body['edad']
    sexo = body['sexo']
    peso = body['peso']
    altura = body['altura']
    restricciones_alimenticias = body['restricciones_alimenticias']

    id = str(int(users[-1].id) + 1) #aca hay que crear la funcion para que cree ID randoms
    #esta funcion sirve para agarrar el ID del usuario anterior y sumarle 1

    nuevo_usuario = Usuario(nombre, contrasena, edad, sexo, peso, altura, restricciones_alimenticias)
    nuevo_usuario.id = id #le agrego el atributo ID

    users.append(nuevo_usuario) #agrega el objeto a la lista users

    return jsonify({'nuevo_usuario': nuevo_usuario.serialize(), 'status': 'creado'}) #devuelve en la API un diccionario que te muestra al nuevo objeto


@app.route("/eliminar_usuario/<ID>", methods=['DELETE'])
def eliminar_usuario(ID):
    for u in users:
        if u.id == ID:
            users.remove(u)
            return jsonify({'Usuario': u.serialize(),
                            'status': 'eliminado'})

            return jsonify({'Usuario': u.serialize(),
                            'status': 'not found'})
