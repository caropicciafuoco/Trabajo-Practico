import uuid


class User:
    def __init__(self, name, password, age, gender, weight, height, intolerance):
        self.id = (str(uuid.uuid4()))[:8]
        self.name = name
        self.password = password
        self.age = int(age)
        self.gender = gender.upper()
        self.weight = int(weight)
        self.height = float(height)
        self.intolerance = intolerance

    def __str__(self):
        return f'\n\tNombre: {self.name}' \
               f'\n\tEdad: {self.age}' \
               f'\n\tPeso: {self.weight}' \
               f'\n\tAltura: {self.height}' \
               f'\n\tSexo: {self.gender}'\
               f'\n\tIntolerancia: {self.intolerance}'

    def serialize(self):
        return {
            'ID': self.id,
            'nombre': self.name,
            "password": self.password,
            'age': self.age,
            'weight': self.weight,
            'height': self.height,
            'gender': self.gender,
            "intolerance": self.intolerance
                }  # lo transforma en diccionario para poder pasarlo a json en el "POST"
