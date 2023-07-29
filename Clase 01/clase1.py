#Esto es un comentario de una línea

#Imprimir
print("Hola mundo")

#Declaración de variable
v1 = 10

#Impresión concatenada
print("Mi variable es: ", v1, "quetzales")

texto = "texto de ejemplo"

print(texto)

"""
Comentario
multilínea
"""

#Impresión avanzada
print(f"valor inicial: {v1} {v1} {v1}")

#Impresión con casteo de int a string
print("valor inicial: " + str(v1))


texto = "cambió el texto"
print(texto)

variable1 = v1 * 55 / 100
print(variable1)

decimal = 55.25
print(decimal)

booleano1 = True
booleano2 = False

print(booleano1, booleano2)


#Listas

#Declaración de una lista
lista1 = [1, "hola", 3.5]
#Impresión lista completa
print(lista1)

#Impresión de un elemento
print(lista1[0])

#Impresión del último elemento de una lista
print(lista1[-1])

#Agregación de un elemento al final de la lista
print(lista1)
lista1.append("5")
print(lista1)

#Tuplas
tupla1 = (1.8, "adiós", 10)
print(tupla1)
#Una tupla no puede ser modificada
#tupla1[0] = 2.5  --> Esto es un error

#Condicionales

#IF
if 1>0:
    print("Verdadero")
else:
    print("falso")

#If - else
condicion = False
if condicion:
    print("V")
else:
    print("F")

#If - else - if
booleanoElif = False
if booleanoElif:
    print("V2")
elif booleanoElif:
    print("F2")
else:
    print("ninguno es cierto")

#Ciclos
#For
for x in range(5, 10):
    print(x)

for i in range(10):
    print(i)

print("-------")
#For para listas, funciona igual para tuplas
listaFor = [5, 8, 9, 15, 50]
for i in listaFor:
    print("valor:", i)

print("-------")
#For para string(str en python)
textoFor = "Texto de ejemplo"
for i in textoFor:
    print("valor:", i)

print("-------")
#Otro for para listas
listaFor = [5, 8, 9, 15, 50]
for i in range(len(listaFor)):
    print("valor:", listaFor[i])


#While
print("----- while -----")
contador = 10
while contador > 0:
    print(contador)
    contador -= 1

#Diccionarios
#Funcionan como clave:valor
diccionario1 = {1:"Valor 1", 2:"valor 2", 3:"valor 3"}
#Obtener un valor a partir de su clave
print(diccionario1[3])

diccionario1 = {"valor1":"Valor 1", "valor2":"valor 2", "valor3":"valor 3"}
print(diccionario1["valor1"])



#For - else
print("------- FOR ELSE ----------")
for i in diccionario1:
    print(diccionario1[i])
else:
    print("Terminó el for-else")

#Funciones
def mifuncion():
    return 80

def suma(a, b, c):
    return a + b + c

def suma2(a: int, b: int, c: int) -> int:
    return a + b + c

#Llamada de funciones
print(mifuncion())
print(suma(10, 50, 60))
print(suma2(10, 50, 60))