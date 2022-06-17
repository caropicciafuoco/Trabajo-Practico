import requests
from receta_class import Receta

@app.route("/obtener_receta/<ID>", methods=['GET'])
def obtener_receta(ID):
    for u in users:
        if u.id == ID:
            lista_intolerancia = u.intolerancia
            parametro_intolerancia = ""

            for intolerancia in lista_intolerancia:
                if parametro_intolerancia == "":
                    parametro_intolerancia += intolerancia
                else:
                    parametro_intolerancia += ",+" + intolerancia

    url_recetas = 'https://api.spoonacular.com/recipes/complexSearch'
    http_rectas = (requests.get(url_recetas, params={'apiKey': 'bebbf46b8c6c4453b8b051dfca6f3f73', 'intolerance': parametro_intolerancia})).json()

    lista_recetas = []

    for r in http_rectas['results']:
        receta = Receta(r['title'], r['id'])
        lista_recetas.append(receta)

    for r in lista_recetas:
        return r


