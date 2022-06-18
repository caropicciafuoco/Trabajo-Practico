from user_class import Usuario

ejemplo = Usuario('J', '1', '22', 'f', '60', '165', 'no')

lista_usuarios = [ejemplo]


def actividad():
    print('\n~ NIVELES DE ACTIVIDAD ~')
    print("\ta. Sedentario/a")
    print("\tb. Poca actividad fisica (1 a 3 veces por semana)")
    print("\tc. Actividad moderada (3 a 5 veces por semana)")
    print("\td. Actividad intensa (6 a 7 veces por semana)")
    print("\te. Atletas profesionales (entrenamientos de más de 4 horas diarias)")

    opcion = input("\n\tIngrese la opcion (a,b,c,d,e) >> ")

    factor_actividad = 0

    if opcion == "a" or opcion == "A":
        factor_actividad += 1.2
        return factor_actividad

    elif opcion == "b" or opcion == "B":
        factor_actividad += 1.375
        return factor_actividad

    elif opcion == "c" or opcion == "C":
        factor_actividad += 1.55
        return factor_actividad

    elif opcion == "d" or opcion == "D":
        factor_actividad += 1.725
        return factor_actividad

    elif opcion == "e" or opcion == "E":
        factor_actividad += 1.9
        return factor_actividad

    else:
        print("Elija una de las opciones indicadas")


def calorias(usuario2):
    for usuario in lista_usuarios:
        if usuario.nombre == usuario2:

            factor_actividad = actividad()

            if usuario.sexo == 'M':
                calorias = (655 + (9.6 * usuario.peso))+((1.8 * usuario.altura) - (4.7 * usuario.edad)) * factor_actividad
                print(f'\n\tCantidad de calorias a ingerir por dia: {calorias}')

            elif usuario.sexo == 'F':
                calorias = (66 + (13.7 * usuario.peso))+((5 * usuario.altura) - (6.8 * usuario.edad)) * factor_actividad
                print(f'\n\tCantidad de calorias a ingerir por dia: {calorias}')

            else:
                print('\nInserte una opcion valida')


def opciones_usuario(usuario2):
    print(f'\nBIENVENIDO/A {usuario2}')
    print('\n¿Que desea realizar?')

    while True:
        print('\t1 - Información personal')
        print('\t2 - Consultar calorias diarias')
        print('\t3 - Obtener una recomendación')
        print('\t4 - Obtener una receta')
        print('\t5 - Salir del usuario')

        option = input('>> ')

        if option == '1':
            for usuario in lista_usuarios:
                if usuario.nombre == usuario2:
                    print(usuario)

        elif option == '2':
            calorias(usuario2)

        elif option == '3':
            pass

        elif option == '4':
            pass

        elif option == '5':
            print('\nSaliendo del usuario...')
            break

        else:
            print('\nIngrese una opcion valida')


def buscar_usuario(usuario2, contraseña2, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario.nombre == usuario2 and usuario.contraseña == contraseña2:
            print('\nIngreso exitoso')
            break
    else:
        print('\nUsuario y/o contraseña invalidos')


def menu_principal():
    print('\n~ Bienvenido a Mundo Fitness ~')
    while True:
        print('\n1 - Crear un usuario')
        print('2 - Ingresar al usuario')
        print('3 - Cerrar programa')

        option = input('>> ')

        if option == '1': #crear usuario
            print('\nComplete con sus datos personales los siguientes items solicitados:')
            nombre = input('\tNombre de usuario >> ')
            contraseña = input('\tContraseña >> ')
            edad = input('\tEdad >> ')
            sexo = input('\tSexo (M o F) >> ')
            peso = input('\tPeso (en kg) >> ')
            altura = input('\tAltura (en cm) >> ')
            intolerancia = (input('\t¿Cuenta con alguna intolerancia? (ingrese si o no) >> ')) #falta poner cual es la restriccion alimenticia

            usuario = Usuario(nombre, contraseña, edad, sexo, peso, altura, intolerancia)

            lista_usuarios.append(usuario)

            print('\nUsuario creado satisfactoriamente')

        elif option == '2': #iniciar sesion
            usuario2 = input('\nIngrese su usuario >> ')
            contraseña2 = input('Ingrese su contraseña >> ')

            buscar_usuario(usuario2, contraseña2, lista_usuarios)

            opciones_usuario(usuario2)

        elif option == '3':
            print('\nCerrando el programa...')
            break

        else:
            print('\nIngrese una opcion valida')

menu_principal()
