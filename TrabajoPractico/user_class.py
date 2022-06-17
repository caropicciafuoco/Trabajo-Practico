class Usuario:
    def __init__(self, nombre, contrasena, edad, sexo, peso, altura, restricciones):
        self.nombre = nombre
        self.contrasena = contrasena
        self.edad = int(edad)
        self.sexo = sexo.upper()
        self.peso = int(peso)
        self.altura = float(altura)
        #self.imc = round(int(self.peso)/int(self.altura)**2, 4)
        self.restricciones = restricciones.lower()

    def __str__(self):
        return f'\n\tNombre: {self.nombre}' \
               f'\n\tEdad: {self.edad}' \
               f'\n\tPeso: {self.peso}' \
               f'\n\tAltura: {self.altura}' \
               f'\n\tSexo: {self.sexo}'\
               f'\n\tRestricciones alimentarias: {self.restricciones}'

    def serialize(self):
        return {
            'nombre': self.nombre,
            "contrasena": self.contrasena,
            "ID": self.id,
            'edad': self.edad,
            'peso': self.peso,
            'altura': self.altura,
            'sexo': self.sexo,
            "restricciones": self.restricciones
                } #lo transforma en diccionario para poder pasarlo a json en el "POST"

#f'\n\tIMC: {self.imc}'\
