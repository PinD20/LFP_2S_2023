from Parser import Parser
from Token import Token

listaTokens = []

def llenarListaTokens():
    listaTokens.clear()
    listaTokens.append(Token('tk_claves', 'Claves', 0, 0))
    listaTokens.append(Token('tk_igual', '=', 0, 0))
    listaTokens.append(Token('tk_corA', '[', 0, 0))
    listaTokens.append(Token('tk_cadena', 'producto', 0, 0))
    listaTokens.append(Token('tk_coma', ',', 0, 0))
    listaTokens.append(Token('tk_cadena', 'cantidad', 0, 0))
    listaTokens.append(Token('tk_corC', ']', 0, 0))

    listaTokens.append(Token('tk_registros', 'Registros', 0, 0))
    listaTokens.append(Token('tk_igual', '=', 0, 0))
    listaTokens.append(Token('tk_corA', '[', 0, 0))

    listaTokens.append(Token('tk_llaveA', '{', 0, 0))
    listaTokens.append(Token('tk_cadena', 'manzana', 0, 0))
    listaTokens.append(Token('tk_coma', ',', 0, 0))
    listaTokens.append(Token('tk_entero', 10, 0, 0))
    listaTokens.append(Token('tk_llaveC', '}', 0, 0))

    listaTokens.append(Token('tk_llaveA', '{', 0, 0))
    listaTokens.append(Token('tk_cadena', 'peras', 0, 0))
    listaTokens.append(Token('tk_coma', ',', 0, 0))
    listaTokens.append(Token('tk_entero', 25, 0, 0))
    listaTokens.append(Token('tk_llaveC', '}', 0, 0))

    listaTokens.append(Token('tk_llaveA', '{', 0, 0))
    listaTokens.append(Token('tk_cadena', 'uvas', 0, 0))
    listaTokens.append(Token('tk_coma', ',', 0, 0))
    listaTokens.append(Token('tk_entero', 315, 0, 0))
    listaTokens.append(Token('tk_llaveC', '}', 0, 0))

    listaTokens.append(Token('tk_corC', ']', 0, 0))

    #Funciones
    listaTokens.append(Token("tk_palabraReservada", "imprimir", 0, 0))
    listaTokens.append(Token("tk_parA", "(", 0, 0))
    listaTokens.append(Token("tk_cadena", "conteo de registros:", 0, 0))
    listaTokens.append(Token("tk_parC", ")", 0, 0))
    listaTokens.append(Token("tk_PyC", ";", 0, 0))

    listaTokens.append(Token("tk_palabraReservada", "conteo", 0, 0))
    listaTokens.append(Token("tk_parA", "(", 0, 0))
    listaTokens.append(Token("tk_parC", ")", 0, 0))
    listaTokens.append(Token("tk_PyC", ";", 0, 0))

    listaTokens.append(Token("tk_palabraReservada", "imprimir", 0, 0))
    listaTokens.append(Token("tk_parA", "(", 0, 0))
    listaTokens.append(Token("tk_cadena", "promedio de cantidad:", 0, 0))
    listaTokens.append(Token("tk_parC", ")", 0, 0))
    listaTokens.append(Token("tk_PyC", ";", 0, 0))

    listaTokens.append(Token("tk_palabraReservada", "promedio", 0, 0))
    listaTokens.append(Token("tk_parA", "(", 0, 0))
    listaTokens.append(Token("tk_cadena", "cantidad", 0, 0))
    listaTokens.append(Token("tk_parC", ")", 0, 0))
    listaTokens.append(Token("tk_PyC", ";", 0, 0))

    '''
    Entrada
    Claves = ["producto", "cantidad"]
    Registros = [
        {"manzana", 10},
        {"peras", 25},
        {"uvas", 315}
    ]
    imprimir("conteo de registros:");
    conteo();
    imprimir("promedio de cantidad:");
    promedio(cantidad);
    '''

if __name__ == '__main__':
    llenarListaTokens()
    parser = Parser(listaTokens)
    parser.parsear()