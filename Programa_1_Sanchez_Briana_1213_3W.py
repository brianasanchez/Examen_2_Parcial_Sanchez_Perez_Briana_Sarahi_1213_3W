print(" ") # print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W") # datos del programador
print(" ") # print imprime un espacio

thislist = ["Matematicas", "Español", "Ecosistemas", "Quimica", "Historia", "Ingles" ] # dando valores a la lista

calificaciones = {} # diccionario vacío

for thislist in thislist: # Hace algo con cada valor de la lista
    calificacion = input(f"Ingrese la calificacion obtenida en {thislist}: ") # pide la calificacion de la materia
    calificaciones[thislist] = calificacion # dando calificacion

print(" ") # print imprime un espacio

x = min(calificaciones) # dando minimo
y = max(calificacion) # dando maximo

if calificacion: # utilizando funcion if
    print(f"Debes recursar la materia de {x}") # print imprime la materia que debe recursar

print(" ") # print imprime un espacio
