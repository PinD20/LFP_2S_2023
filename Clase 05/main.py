# Algoritmos de búsqueda

def busqueda_lineal(objetivo: int, numeros: list):
    for num in numeros:
        if num == objetivo:
            return True
    return False


def busqueda_binaria(objetivo: int, numeros: list, inicio, fin):
    if inicio > fin:
        return False
    #El signo // divide pero redondea a entero
    mitad = (inicio + fin) // 2

    if objetivo == numeros[mitad]:
        return True
    elif objetivo < numeros[mitad]:
        return busqueda_binaria(objetivo, numeros, inicio, mitad - 1)
    else:
        return busqueda_binaria(objetivo, numeros, mitad + 1, fin)



lista = [1,3,5,10,30,100]


#print(busqueda_lineal(11, lista))
print(busqueda_binaria(3, lista, 0, len(lista) - 1))