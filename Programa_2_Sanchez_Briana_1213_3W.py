print(" ") # print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3W") # datos del programador
print(" ") # print imprime un espacio

credito1 = 7 # dando valor a variable
credito2 = 8 # dando valor a variable
credito3 = 9 # dando valor a variable
credito4 = 10 # dando valor a variable 
credito5 = 9 # dando valor a variable 
credito6 = 10 # dando valor a variable

thisdict = { # abriendo diccionario
    "Lengua y Comunicacion :" : 7, # tipo de dato
    "Matematicas :" : 8, # tipo de dato
    "Ecosistemas :" : 9, # tipo de dato
    "Ingles :" : 10, # tipo de dato
    "Humanidades :" : 9, # tipo de dato 
    "Programacion :" : 10, # tipo de dato
} # cerando diccionario

# funcion que recorrer tanto las claves como los valores 
for x, y in thisdict.items():
  print(x, y)

print(" ") # print imprime un espacio

suma = credito1 + credito2 + credito3 + credito4 + credito5 + credito6 # haciendo suma 

print(f"La suma de los creditos es : {suma}.") # print imprime la suma de los creditos

print(" ") # print imprime un espacio