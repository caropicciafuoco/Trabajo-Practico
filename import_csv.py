import json
from io import open
import csv


users = []

with open("usuarios.json", "r") as file:  # para leer el json
    users_json = json.load(file)

    for user in users_json:
        users.append(tuple(user.values()))



with open("csv_users.csv", "w", newline="\n") as archivo:
    campos = ['name', 'password', 'age', 'gender', 'weight', 'height', 'intolerance']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for name, password, age, gender, weight, height, intolerance in users:
        writer.writerow({
            'name': name,
            'password': password,
            'age': age,
            'gender': gender,
            'weight': weight,
            'height': height,
            'intolerance': intolerance})
