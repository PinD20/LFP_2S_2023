class Error():
    def __init__(self, lexema, tipo, columna, fila) -> None:
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.fila = fila

    def __str__(self):
        return f'Lexema: {self.lexema}, tipo: {self.tipo}, fila: {self.fila}, columna: {self.columna}'
    