class Error():
    def __init__(self, lexema, tipo, columna, fila) -> None:
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.fila = fila