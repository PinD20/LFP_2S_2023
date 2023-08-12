#CONTINUACIÓN DE ARCHIVOS

#Permisos de apertura de archivos
#Sólo lectura (r)
#Sólo escritura (w)
#Sólo escritura posicionándose al final del archivo (a)

#Escritura de archivos
archivo = open("texto.txt", "a")

archivo.write("Texto agregado desde Python 3.\n")

archivo.close()





#Algoritmos de ordenamiento

def ordenamiento_burbuja(numeros: list):
    n = len(numeros)
    for i in range(n):
        for j in range(n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

def ordenamiento_burbuja_2(numeros: list):
    intercambio = True #True para que entre al menos una vez al while
    while intercambio:
        intercambio = False
        for i in range(len(numeros) - 1):#0 - 4: 3
            if numeros[i] > numeros[i + 1]:
                numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
                intercambio = True

def ordenamiento_insercion(numeros: list):
    for i in range(1, len(numeros)):
        valor_actual = numeros[i]
        indice_actual = i
        while indice_actual > 0 and numeros[indice_actual - 1] > valor_actual:
            numeros[indice_actual] = numeros[indice_actual - 1]
            indice_actual -= 1
        numeros[indice_actual] = valor_actual

def ordenamiento_seleccion(numeros: list):
    for i in range(len(numeros)): #1
        indice_valor_menor = i
        for j in range(i + 1, len(numeros)):#2
            if numeros[j] < numeros[indice_valor_menor]:
                indice_valor_menor = j
        numeros[i], numeros[indice_valor_menor] = numeros[indice_valor_menor], numeros[i]

lista = [16, 5, 7, 2, 15]
ordenamiento_seleccion(lista)

print(lista)