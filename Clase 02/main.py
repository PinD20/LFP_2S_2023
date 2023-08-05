'''
#Main
if __name__ == "__main__":
    print("es un main")


#En Python el tipo de variable puede cambiar
v1 = 2
print(v1)
v1 = "string"
print(v1)
v1 = 2.5
print(v1)


#Divisón siempre da un float en Python
print(1/1)
print(1.2/1)
print(1/1.9)
print(1.8/1.7)
'''


def abrirConRuta():
    ruta = input("Ingrese la ruta del archivo: ")
    archivo = open(ruta, "r", encoding="utf-8")

    print(archivo.read())
    archivo.close()


def abrirArchivo():
    #Abrir archivo
    archivo = open("texto.txt", "r", encoding="utf-8")

    #Obtener el texto del archivo
    #texto = archivo.read()
    
    #Leer una línea del archivo
    print(archivo.readline())

    #Leer un caracter de una línea del archivo
    #print(archivo.readline(1))

    #Cerrar archivo
    archivo.close()




arch = open ("prueba.aver")

#txt = arch.read()
#Recorrer caracter por caracter un string
#for i in txt:
#    print(i)


#Lista de líneas del archivo
#print(arch.readlines())


#Para el archivo .inv, porque no importa reconocer la palabra crear_producto
listaDatos = []
#Recorrer las líneas del archivo
for linea in arch.readlines():
    aux = linea.split(" ")
    aux2 = aux[1].split("=")
    valor_con_salto_linea = aux2[1]
    listaDatos.append([aux2[0], valor_con_salto_linea.strip("\n")])

arch.close()

print(listaDatos)



ints = []
floats = []

arch2 = open ("prueba.aver")
for linea2 in arch2.readlines():
    aux = linea2.split(" ") # aux queda como una lista que tiene ["int", "variable=5"]
    aux2 = aux[1].split("=") #2 aux queda como una lista que tiene ["variable", "5"]
    valor_con_salto_linea = aux2[1]

    if aux[0].startswith("int"):#Aquí se verifica con qué palabra comenzaba la línea
        #En vez de una lista, podrían tener un método a donde mandar sus datos de agregar stock
        ints.append([aux2[0], valor_con_salto_linea.strip("\n")])
    else:
        #En vez de una lista, podrían tener un método a donde mandar sus datos de venta
        floats.append([aux2[0], valor_con_salto_linea.strip("\n")])

arch2.close()

print("enteros")
print(ints)

print("decimales")
print(floats)


#Recibir datos por consola
#entrada = input("Ingrese la ruta del archivo: ")
#print(entrada)


#Objetos

#Creación de la clase
class MiObjeto:
    def __init__(self, parametro1, parametro2) -> None:
        self.nombre = parametro1
        self.apellido = parametro2


#Instanciar un objeto
objetito = MiObjeto("Juabn", "Pérez")

#Cambiar atributos de un objeto
objetito.nombre = "José"

#Acceder a atributo de objeto
print(objetito.nombre)