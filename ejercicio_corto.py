''' Desarrolle una función que reciba una lista de usuarios con nombre, edad, rol, profesión, sueldo y
retorne solo los usuarios mayores de edad cuyo rol sea empleado o estudiante, ordenados por
edad de menor a mayor, sueldos de mayor a menor.'''

# Definición de usuarios
usuario1 = {
    "nombre": "MIGUEL",
    "edad": 40,
    "rol": "Empleado",
    "profesion": "Ingeniero",
    "sueldo": 5000
}

usuario2 = {
    "nombre": "ZULMA",
    "edad": 38,
    "rol": "Empleado",
    "profesion": "Contadora",
    "sueldo": 4500
}

usuario3 = {
    "nombre": "LUIS",
    "edad": 17,
    "rol": "Estudiante",
    "profesion": "Estudiante",
    "sueldo": 0
}

usuario4 = {
    "nombre": "ABIGAIL",
    "edad": 16,
    "rol": "Estudiante",
    "profesion": "Diseñadora",
    "sueldo": 3000
}

usuario5 = {
    "nombre": "CARLOS",
    "edad": 45,
    "rol": "Empleado",
    "profesion": "Administrador",
    "sueldo": 7000
}
#lista de usuarios
lista_usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5]

def filtrar_usuarios():
    # Lista para almacenar los usuarios filtrados y ordenados
    lista_ordenada = []
    # Filtrar y ordenar usuarios según los criterios dados
    for usuario in lista_usuarios:
        if usuario["edad"]>=18 and usuario["rol"] in ["Empleado", "Estudiante"]:
            lista_ordenada.append(usuario)
            lista_ordenada = sorted(lista_ordenada, key=lambda x: (x["edad"], -x["sueldo"]))# Ordenar por edad ascendente y sueldo descendente
    # Imprimir los usuarios filtrados y ordenados
    for usuario in lista_ordenada:
        print(usuario)
    
filtrar_usuarios()