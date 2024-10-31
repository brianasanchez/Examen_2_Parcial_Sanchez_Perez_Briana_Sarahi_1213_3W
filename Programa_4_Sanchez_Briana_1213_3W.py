print(" ") # print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W") # datos del programador
print(" ") # print imprime un espacio

nombre = input("¿Cual es tu nombre? ") # pide que ingreses tu nombre
edad = input("¿Cual es tu edad? ") # pide que ingreses tu edad
direccion = input("¿Donde vives? ") # pide que ingreses tu direccion
telefono = input("¿Cual es tu numero de telefono? ") # pide que ingreses tu numero de telefono

print(" ") # print imprime un espacio

thisdict = { # abriendo diccionario
    "nombre": nombre, #  dando tipos de datos 
    "edad": edad, #  dando tipos de datos 
    "direccion": direccion, #  dando tipos de datos 
    "telefono": telefono #  dando tipos de datos 
} # cerrando diccionario

print(f"{thisdict['nombre']} tiene {thisdict['edad']} años,") # print imprime el nombre y la edad ingresada
print(f"vive en {thisdict['direccion']}") # print imprime la direccion ingresada
print(f"y su número de teléfono es {thisdict['telefono']}.") # print imprime el numero de telefono ingresado

print(" ") # print imprime un espacio

