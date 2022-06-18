import json
from io import open
from user_class import Usuario

def load_users():
    users = []

    with open("TrabajoPractico/usuarios.json", "r") as file: #para leer el json
        users_json = json.load(file)

        for user in users_json:

            new_user = Usuario(
                                user["nombre"],
                                user["contrasena"],
                                user["edad"],
                                user["sexo"],
                                user["peso"],
                                user["altura"],
                                user["intolerancia"]
                                )

            users.append(new_user)

    return users


# Para probar si funciona: print(load_users()[2])
#for usuario in load_users():
    #print(usuario)