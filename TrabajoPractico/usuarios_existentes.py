from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios_existentes = [
               {"nombre":"Carla Estevez",
                "ID": "1",
                "contraseña":"Carla123",
                "edad":"45",
                "sexo":"F",
                "peso": "90",
                "altura":"1.60",
                "restricciones_alimenticias": None},

                {"nombre":"Dona Terra",
                "ID": "2",
                "contraseña":"Dona123",
                "edad":"33",
                "sexo":"F",
                "peso": "66",
                "altura":"1.63",
                "restricciones_alimenticias": "Vegetariana"},

                {"nombre":"Juan Martinelli",
                "ID": "3",
                "contraseña":"Juan123",
                "edad":"21",
                "sexo":"M",
                "peso": "42",
                "altura":"1.80",
                "restricciones_alimenticias": None},

                {"nombre":"Tomas Milke",
                "ID": "4",
                "contraseña":"Tomas123",
                "edad":"19",
                "sexo":"M",
                "peso": "68",
                "altura":"1.83",
                "restricciones_alimenticias":"Alergico al mani"},

                {"nombre":"Robbie Bey",
                "ID": "5",
                "contraseña":"Robbie123",
                "edad":"13",
                "sexo":"M",
                "peso": "26",
                "altura":"1.63",
                "restricciones_alimenticias": "Celiaco"},

                {"nombre":"Claudia Tros",
                "ID": "6",
                "contraseña":"Claudia123",
                "edad":"60",
                "sexo":"F",
                "peso": "120",
                "altura":"1.50",
                "restricciones_alimenticias": None},

                {"nombre":"Emma Bindel",
                "ID": "7",
                "contraseña":"Emma123",
                "edad":"20",
                "sexo":"F",
                "peso": "40",
                "altura":"1.42",
                "restricciones_alimenticias": "Alergica al tomate"},

                {"nombre":"Kiara Perkins",
                "ID": "8",
                "contraseña":"Kiara123",
                "edad":"13",
                "sexo":"F",
                "peso": "26",
                "altura":"1.61",
                "restricciones_alimenticias": None},

                {"nombre":"Gal Sortes",
                "ID": "9",
                "contraseña":"Gal123",
                "edad":"23",
                "sexo":"F",
                "peso": "46",
                "altura":"1.43",
                "restricciones_alimenticias": "Celiaca"},

                {"nombre":"Mijal Benitez",
                "ID": "10",
                "contraseña":"Mijal123",
                "edad":"15",
                "sexo":"F",
                "peso": "30",
                "altura":"1.45",
                "restricciones_alimenticias": "Vegana"},

                {"nombre":"Kevin Tel",
                "ID": "11",
                "contraseña":"Kevin123",
                "edad":"50",
                "sexo":"M",
                "peso": "100",
                "altura":"1.70",
                "restricciones_alimenticias": "Intolerante a la lactosa"},

                {"nombre":"Maximo Zas",
                "ID": "12",
                "contraseña":"Maximo123",
                "edad":"53",
                "sexo":"M",
                "peso": "114",
                "altura":"1.54",
                "restricciones_alimenticias": "Vegetariano"},

                {"nombre":"Yanina Arias",
                "ID": "13",
                "contraseña":"Yanina123",
                "edad":"90",
                "sexo":"F",
                "peso": "180",
                "altura":"1.78",
                "restricciones_alimenticias": "Alergica a la palta"},

                {"nombre":"Tamara Ruiz",
                "ID": "14",
                "contraseña":"Tamara123",
                "edad":"86",
                "sexo":"F",
                "peso": "70",
                "altura":"1.78",
                "restricciones_alimenticias": "Vegetariana"},

                {"nombre":"Solana Jaichenco",
                "ID": "15",
                "contraseña":"Solana123",
                "edad":"57",
                "sexo":"F",
                "peso": "58",
                "altura":"1.75",
                "restricciones_alimenticias": None},

                {"nombre":"Magali Ringler",
                "ID": "16",
                "contraseña":"Magali123",
                "edad":"49",
                "sexo":"F",
                "peso": "50",
                "altura":"1.59",
                "restricciones_alimenticias": None},

                {"nombre":"Valentina Pinto",
                "ID": "17",
                "contraseña":"Valentina123",
                "edad":"10",
                "sexo":"F",
                "peso": "73",
                "altura":"1.71",
                "restricciones_alimenticias": None},

                {"nombre":"Federico Jaraj",
                "ID": "18",
                "contraseña":"Federico123",
                "edad":"94",
                "sexo":"M",
                "peso": "60",
                "altura":"2.00",
                "restricciones_alimenticias": None},

                {"nombre":"Gaston Madrin",
                "ID": "19",
                "contraseña":"Gaston123",
                "edad":"66",
                "sexo":"M",
                "peso": "82",
                "altura":"1.62",
                "restricciones_alimenticias": "Celiaco"},

                {"nombre":"Gabriel Perez",
                "ID": "20",
                "contraseña":"Gabriel123",
                "edad":"44",
                "sexo":"M",
                "peso": "88",
                "altura":"1.84",
                "restricciones_alimenticias": "Intolerante a la verdura cruda"},

                {"nombre":"Daniel Lincoln",
                "ID": "21",
                "contraseña":"Daniel123",
                "edad":"87",
                "sexo":"M",
                "peso": "67",
                "altura":"1.76",
                "restricciones_alimenticias": "Vegano"},

                {"nombre":"Victor Leda",
                "ID": "22",
                "contraseña":"Victor123",
                "edad":"30",
                "sexo":"M",
                "peso": "60",
                "altura":"1.63",
                "restricciones_alimenticias": "Alergico a la nuez"},

                {"nombre":"Adrian Lucero",
                "ID": "23",
                "contraseña":"Adrian123",
                "edad":"40",
                "sexo":"M",
                "peso": "86",
                "altura":"1.64",
                "restricciones_alimenticias": "Vegetariano"},

                {"nombre":"Leandro Repis",
                "ID": "24",
                "contraseña":"Leandro123",
                "edad":"29",
                "sexo":"M",
                "peso": "58",
                "altura":"1.50",
                "restricciones_alimenticias": None},

                {"nombre":"Martina Teitel",
                "ID": "25",
                "contraseña":"Martina123",
                "edad":"22",
                "sexo":"F",
                "peso": "63",
                "altura":"1.62",
                "restricciones_alimenticias": None},

                {"nombre":"Mariana Piczman",
                "ID":"26",
                "contraseña":"Mariana123",
                "edad":"58",
                "sexo":"F",
                "peso": "65",
                "altura":"1.85",
                "restricciones_alimenticias": None},

                {"nombre":"Veronica Jarosky",
                "ID":"27",
                "contraseña":"Veronica123",
                "edad":"9",
                "sexo":"F",
                "peso": "25",
                "altura":"1.35",
                "restricciones_alimenticias": None},

                {"nombre":"Mora Glit",
                "ID":"28",
                "contraseña":"Mora123",
                "edad":"63",
                "sexo":"F",
                "peso": "59",
                "altura":"1.68",
                "restricciones_alimenticias": None},

                {"nombre":"Nicole Tokla",
                "ID":"29",
                "contraseña":"Nicole123",
                "edad":"95",
                "sexo":"F",
                "peso": "53",
                "altura":"1.66",
                "restricciones_alimenticias": None},

                {"nombre":"Martin Blarg",
                "ID":"30",
                "contraseña":"Martin123",
                "edad":"37",
                "sexo":"M",
                "peso": "94",
                "altura":"1.95",
                "restricciones_alimenticias": "Vegano"}

]

@app.route("/info_usuario/<id>", methods=['GET'])
def usuario_get(id):#hay que poner nombres diferentes en lasfunciones
    for u in usuarios_existentes:
        if u['ID'] == id:
            return jsonify({"Nombre":u['nombre'],"Sexo":u['sexo'],"Edad": u['edad'],"Altura":u['altura'],
                           "Peso":u['peso'],"Restriccion Alimenticias":u['restricciones_alimenticias'], "status": "existente"})
    return jsonify({"busqueda": id, "status": "not found"})

@app.route("/crear_usuario", methods=['POST'])

def crear_usario():
   body = request.json
   nombre = body['nombre']
   id = str(int(usuarios_existentes[-1]["ID"]) + 1)
   contraseña = body['contraseña']
   edad = body['edad']
   sexo = body['sexo']
   peso = body['peso']
   altura = body['altura']
   restricciones_alimenticias =body['restricciones_alimenticias']

   nuevo_usuario = {'nombre': nombre, 'ID': id,'contraseña': contraseña, 'edad':edad, 'sexo': sexo, 'peso':peso, 'altura': altura,'restricciones_alimenticias':restricciones_alimenticias}

   usuarios_existentes.append(nuevo_usuario)
   return jsonify({'nuevo_usuario': nuevo_usuario, 'status': 'creado'})