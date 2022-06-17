from flask import Flask, jsonify, request

from User_loader import load_users
from usuario import Usuario

app = Flask(__name__)
users = load_users()


@app.route("/usuarios", methods=['GET'])
def usuarios():  # hay que poner nombres diferentes en lasfunciones
    return jsonify([user.serialize() for user in users])
    # return jsonify({"Usuarios": users})


@app.route("/info_usuario/<ID>", methods=['GET'])
def usuario_get(ID):  # hay que poner nombres diferentes en lasfunciones
    for u in users:
        if u.id == ID:
            return jsonify({"Nombre": u.nombre,
                            "Sexo": u.sexo,
                            "Edad": u.edad,
                            "Altura": u.altura,
                            "Peso": u.peso,
                            "Restriccion Alimenticias": u.restricciones,
                            "status": "existente"})

    return jsonify({"ID buscado": ID,
                    "status": "not found"})


@app.route("/crear_usuario", methods=['POST'])
def crear_usario():
    body = request.json
    nombre = body['nombre']
    id = str(int(users[-1].id) + 1)
    contrasena = body['contrasena']
    edad = body['edad']
    sexo = body['sexo']
    peso = body['peso']
    altura = body['altura']
    restricciones_alimenticias = body['restricciones_alimenticias']

    nuevo_usuario = Usuario(nombre, contrasena, edad, sexo, peso, altura, restricciones_alimenticias)
    nuevo_usuario.id = id

    users.append(nuevo_usuario)

    return jsonify({'nuevo_usuario': nuevo_usuario.serialize(), 'status': 'creado'})


@app.route("/eliminar_usuario/<ID>", methods=['DELETE'])
def eliminar_usuario(ID):
    for u in users:
        if u.id == ID:
            users.remove(u)
            return jsonify({'Usuario': u.serialize(),
                            'status': 'eliminado'})

            return jsonify({'Usuario': u.serialize(),
                            'status': 'not found'})
