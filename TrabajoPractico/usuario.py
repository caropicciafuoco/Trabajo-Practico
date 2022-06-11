class Usuario:
    def __init__(self, nombre, contraseña, edad, sexo, peso, altura, restricciones):
        self.nombre = nombre
        self.contraseña = contraseña
        self.edad = int(edad)
        self.sexo = sexo.upper()
        self.peso = int(peso)
        self.altura = int(altura)
        #self.imc = round(int(self.peso)/int(self.altura)**2, 4)
        self.restricciones = restricciones.lower()

    def __str__(self):
        return f'\n\tNombre: {self.nombre}' \
               f'\n\tEdad: {self.edad}' \
               f'\n\tPeso: {self.peso}' \
               f'\n\tAltura: {self.altura}' \
               f'\n\tSexo: {self.sexo}'\
               f'\n\tRestricciones alimentarias: {self.restricciones}'

#f'\n\tIMC: {self.imc}'\
