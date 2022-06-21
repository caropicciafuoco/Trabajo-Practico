import json
from io import open
from user_class import User


def load_users():
    users = []

    with open("usuarios.json", "r") as file:  # para leer el json
        users_json = json.load(file)

        for user in users_json:
            new_user = User(user["name"], user["password"], user["age"], user["gender"], user["weight"], user["height"],
                            user["intolerance"])

            users.append(new_user)

    return users

# Para probar si funciona: print(load_users()[2])
# for usuario in load_users():
#       print(usuario)
