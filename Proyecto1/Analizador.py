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

from Error import Error
from Token import Token

class Analizador():
    def __init__(self, texto) -> None:
        self.texto = texto
        self.tokens_reconocidos = []
        self.errores = []

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
        columna = 1

        estado = 0
        estado_anterior = 0
        lexema = ""

        self.tokens_reconocidos = []
        self.errores = []

        #Análisis de caracter por caracter
        for caracter in self.texto:
            ascii = ord(caracter)
            if estado == 0:
                if ascii == 34:
                    lexema += caracter
                    estado = 1
                    estado_anterior = 0
                elif caracter.isdigit():
                    lexema += str(caracter)
                    estado = 2
                    estado_anterior = 0
                elif self.isSimboloValido(ascii):
                    lexema += caracter
                    estado = 10
                    estado_anterior = 0
                else:
                    #Se omiten espacios, tabulaciones y saltos de línea
                    if ascii == 32 or ascii == 9 or ascii == 10:
                        pass
                    else:
                        #error
                        self.errores.append(Error(caracter, 'Léxico', columna - len(lexema), fila))
                    
                    #Reinicio del lexema
                    lexema = ""
                    estado = 0
                    estado_anterior = 0
            elif estado == 1:
                if ascii == 34:
                    lexema += caracter
                    estado = 10
                    estado_anterior = 1
                elif ascii != 10:
                    lexema += caracter
                    estado = 1
                    estado_anterior = 1
                else:
                    self.errores.append(Error(lexema, 'Léxico', columna - len(lexema), fila))
                    #Reinicio del lexema
                    lexema = ""
                    estado = 0

            elif estado == 2:
                if caracter.isdigit():
                    lexema += str(caracter)
                    estado = 2
                    estado_anterior = 2
                else:#Es estado de aceptación entonces se guarda token
                    self.tokens_reconocidos.append(Token('Entero', int(lexema), fila, columna - len(lexema)))
                    lexema = ""
                    if ascii == 9 or ascii == 10 or ascii == 32:
                        pass
                    elif self.isSimboloValido(ascii):
                        lexema += caracter
                        estado = 10
                        estado_anterior = 0
                    elif ascii == 34:
                        lexema += caracter
                        estado = 1
                        estado_anterior = 0
                    else:#Error
                        self.errores.append(Error(caracter, 'Léxico', columna - len(lexema), fila))
                    #Reinicio del lexema
                    lexema = ""
                    estado = 0
            
            elif estado == 10:
                if estado_anterior == 0 or estado_anterior == 2:
                    self.tokens_reconocidos.append(Token('Signo', lexema, fila, columna - len(lexema)))
                elif estado_anterior == 1:
                    self.tokens_reconocidos.append(Token('String', lexema, fila, columna - len(lexema)))

                lexema = ""
                if ascii == 34:
                    lexema += caracter
                    estado = 1
                    estado_anterior = 0
                elif caracter.isdigit():
                    lexema += str(caracter)
                    estado = 2
                    estado_anterior = 0
                elif self.isSimboloValido(ascii):
                    lexema += caracter
                    estado = 10
                    estado_anterior = 0
                else:
                    #Se omiten espacios, tabulaciones y saltos de línea
                    if ascii == 32 or ascii == 9 or ascii == 10:
                        pass
                    else:
                        #error
                        self.errores.append(Error(caracter, 'Léxico', columna - len(lexema), fila))
                    
                    #Reinicio del lexema
                    lexema = ""
                    estado = 0
                    estado_anterior = 0


            #Control de lineas y columnas 

            #Salto de línea
            if ascii == 10:
                fila += 1
                columna = 1
                continue
            #Tabulación
            elif ascii == 9:
                columna += 4
                continue
            #Espacio
            elif ascii == 32:
                columna += 1
                continue
            

            columna += 1

#Validar fin del texto

                        

