'''
Tokens válidos
    {
    }
    [
    ]
    string  -->  " lo que sea menos un salto de línea "
    enteros --> 0-9
    coma --> ,
    dos_puntos --> :

    Estados: S0, S1, S2, S10
    S0: inicio
    S10: finalización

    S0  { } [ ] , : --> S10
        "           --> S1
        0-9         --> S2
        
        ? --> Error
        + --> Error
        Error (si viene algo distinto)


    S1  "           --> S10
        (cualquier cosa excepto salto linea) --> S1
        
    S2  0-9         --> S2
        cualquier_otro --> S10


'''

class Analizador():
    def __init__(self, texto) -> None:
        self.texto = texto

    '''
    def isNumero(self, ascii):
        if ascii > 47 and ascii < 57:
            return True
        return False
    '''
    
    def isSimboloValido(self, ascii):
        if ascii == 123 or ascii == 125 or ascii == 91 or ascii == 93 or ascii == 44 or ascii == 58:
            return True
        return False

    def analizar(self):
        fila = 1
        columa = 1

        estado = 0
        lexema = ""

        tokens_reconocidos = []

        #Análisis de caracter por caracter
        for caracter in self.texto:
            ascii = ord(caracter)
            if estado == 0:
                if ascii == 34:
                    lexema += caracter
                    estado = 1
                elif caracter.isDigit():
                    lexema += caracter
                    estado = 2
                elif self.isSimboloValido(ascii):
                    lexema += caracter
                    estado = 10
                else:
                    #Se omiten espacios, tabulaciones y saltos de línea
                    if ascii == 32 or ascii == 9 or ascii == 10:
                        pass
                    else:
                        #error
                        pass
                    lexema = ""
                    estado = 0
            elif estado == 1:
                pass



            #Control de lineas y columnas 
                        

