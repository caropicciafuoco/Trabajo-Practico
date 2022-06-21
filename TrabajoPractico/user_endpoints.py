from flask import Flask, jsonify, request

from user_loader import load_users
from user_class import User

import requests
from recipe_class import Recipe


app = Flask(__name__)
users = load_users()


@app.route("/users", methods=['GET'])
def get_users():
    return jsonify([user.serialize() for user in users])
    # return jsonify({"Usuarios": users})


@app.route("/user_info/<ID>", methods=['GET'])
def user_info(ID):
    for u in users:
        if u.id == ID:
            return jsonify({"Name": u.name,  # Se usa el punto para acceder al objeto
                            "Gender": u.gender,
                            "Age": u.age,
                            "Height": u.height,
                            "Weight": u.weight,
                            "Intolerances": u.intolerance})

    return jsonify({"Look up ID": ID,
                    "Status": "Not found"})

# Se usa jsonify para transformar diccionarios a json y es necesario porque la API solo trabaja con json


@app.route("/create_user", methods=['POST'])
def create_user():
    body = request.json  # Simboliza el body de postman
    name = body['name']
    password = body['password']
    age = body['age']
    gender = body['gender']
    weight = body['weight']
    height = body['height']
    intolerances = body['intolerances']

    new_user = User(name, password, age, gender, weight, height, intolerances)

    users.append(new_user)  # Agrega el objeto a la lista users

    return jsonify({'new_user': new_user.serialize(), 'status': 'created'})  # Devuelve en la API un diccionario
    # que te muestra al nuevo objeto


'''
Usuario de prueba para postman:
    {
        "name": "Carolina Picciafuoco",
        "password": "hbflwhd",
        "age": "19",
        "gender": "F",
        "weight": "50",
        "height": "1.60",
        "intolerances": []
    }
'''


@app.route("/delete_user/<ID>", methods=['DELETE'])
def delete_user(ID):
    for u in users:
        if u.id == ID:
            users.remove(u)
            return jsonify({'User': u.serialize(),
                            'Status': 'Removed'})

    return jsonify({'Look up ID': ID,
                    'Status': 'Not found'})


@app.route("/change_weight", methods=['PUT'])
def change_weight():
    body = request.json
    ID = body['id']
    new_weight = body['weight']

    for u in users:
        if u.id == ID:
            u.weight = new_weight
            return jsonify({'User': u.serialize(),
                            'New Weight': u.weight,
                            'Status': 'Weight has been updated'})

    return jsonify({'Look up ID': ID,
                    'Status': 'Not found'})


'''
Prueba para postman
    {
        "id": "",
        "weight": 70
    }
'''


@app.route("/change_password", methods=['PUT'])
def change_password():
    body = request.json
    ID = body['id']
    new_password = body['password']

    for u in users:
        if u.id == ID:
            u.password = new_password
            return jsonify({'User': u.serialize(),
                            'New Password': new_password,
                            'Status': 'Password has been updated'})

    return jsonify({'ID buscado': ID,
                    'Status': 'Not found'})


'''
Prueba para postman:
    {
        "id": "",
        "password": "holamundo"
    }
'''


@app.route("/get_recipes/<ID>", methods=['GET'])
def get_recipes(ID):
    url_recipes = 'https://api.spoonacular.com/recipes/complexSearch'
    param_intolerance = ''

    for u in users:
        if u.id == ID:
            for intolerance in u.intolerance:
                if param_intolerance == '':
                    param_intolerance += intolerance
                else:
                    param_intolerance += ',+' + intolerance

    http_recipes = (requests.get(url_recipes, params={'apiKey': 'bebbf46b8c6c4453b8b051dfca6f3f73',
                                                      'intolerance': param_intolerance, 'number': 5})).json()

    recipe_list = []

    for r in http_recipes['results']:
        url_complete_recipe = f"https://api.spoonacular.com/recipes/{r['id']}/information"
        http_complete_recipe = (requests.get(url_complete_recipe,
                                             params={'apiKey': 'bebbf46b8c6c4453b8b051dfca6f3f73'})).json()

        title = http_complete_recipe['title']
        id = http_complete_recipe['id']
        servings = http_complete_recipe['servings']
        cooking_time = str(http_complete_recipe['readyInMinutes']) + ' minutes'

        ingredients_list = []

        for ingredient in http_complete_recipe['extendedIngredients']:
            ingredients_list.append(ingredient['original'])

        recipe = Recipe(title, id, servings, cooking_time, ingredients_list)

        recipe_list.append(recipe)

    return jsonify([r.serialize() for r in recipe_list])
