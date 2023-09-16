from Analizador import Analizador
from tkinter import filedialog, Tk

def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title= "Seleccionar un archivo json",
        initialdir= "./",
        filetypes = (
            ("Archivos JSON", "*.json"),
            ("Todos los archivos",  "*.*")
        )
    )
    if archivo == '':
        print('No se seleccionó ningun archivo\n')
        return None
    else:
        doc = open(archivo,'r', encoding='utf-8')
        texto = doc.read()
        return texto
    
def reconocerOperacion(lista):
    resultado = 0
    tipoOperacion = lista[3].lexema
    (numero1, lista) = obtenerValor(lista[7:])
    
    if lista[0].lexema == ",":#Viene otro valor
        (numero2, lista) = obtenerValor(lista[3:])
        
        if tipoOperacion == '"suma"':
            resultado = numero1 + numero2
            #print(numero1, "+", numero2, "=", resultado)
        elif tipoOperacion == '"resta"':
            resultado = numero1 - numero2
            #print(numero1, "-", numero2, "=", resultado)

    else:
        #Viene sólo 1 valor en la operación
        pass
    
    #En la lista se retira la llave que cierra la operación
    return (resultado, lista[1:])


def obtenerValor(lista):
    numeroFinal = 0
    listaNueva = []
    try:#si guardaron el tipo de token no es necesario el try except, sería solo un IF
        numeroFinal = float(lista[0].lexema)
        listaNueva = lista[1:]
    except:#Operacion anidada
        #Estructura de una anidada: [ { operacion, valor1, valor2 } ]
        #Para enviarlo como operación primero se quita el corchete de apertura
        (numeroFinal, lista) = reconocerOperacion(lista[1:])
        #Luego se quita el corchete de cierre
        listaNueva = lista[1:]

    return (numeroFinal, listaNueva)

if __name__ == '__main__':
    txt = abrir()
    if txt is not None:
        lexer = Analizador(txt)
        lexer.analizar()
        lista = lexer.tokens_reconocidos[4:]
        estado = "operaciones"

        contador = 0
        while True:
            if len(lista) == 0: break

            if estado == "operaciones":
                (resultado, lista) = reconocerOperacion(lista)
                
                contador += 1
                print("Resultado operación", contador, ":", resultado)

                if lista[0].lexema == "]": #Terminan las operaciones
                    estado = "configuraciones"
                    lista = lista[2:]#Se quita el token con el corchete de cierre la lista de operaciones y la coma
                else: #Viene otra operación
                    lista = lista[1:]#Se quita el token coma que separa la sig operación
            elif estado == "configuraciones":
                break#Termina porque configuraciones es lo último
            


        #print("--------------------------- Tokens ---------------------------")
        #for i in lexer.tokens_reconocidos:
        #    print(i)
        #print("--------------------------- Errores ---------------------------")
        #for i in lexer.errores:
        #    print(i)
    else:
        print(":(")