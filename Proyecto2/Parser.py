from Token import Token

class Parser():
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.listaClaves = []
        self.listaRegistros = []

        #Controlar que se llegó al final de la lista de tokens
        tokenNuevo = Token('EOF', 'EOF', 0, 0)
        self.tokens.append(tokenNuevo)

    def recuperar(self, nombreToken):
        while self.tokens[0].nombre != 'EOF':
            if self.tokens[0].nombre == nombreToken:
                self.tokens.pop(0)
                break
            else:
                self.tokens.pop(0)

    def recuperarDos(self, nombreToken1, nombreToken2):
        while self.tokens[0].nombre != 'EOF':
            if self.tokens[0].nombre == nombreToken1 or self.tokens[0].nombre == nombreToken2:
                self.tokens.pop(0)
                break
            else:
                self.tokens.pop(0)

    def parsear(self):
        self.inicio()

    #<inicio> ::= <claves> <registros> <funciones>
    def inicio(self):
        self.claves()
        self.registros()
        self.funciones()

    #<claves> ::= tk_claves tk_igual tk_corA tk_cadena <otra_clave> tk_corC
    def claves(self):
        if self.tokens[0].nombre == 'tk_claves':
            self.tokens.pop(0)
            if self.tokens[0].nombre == 'tk_igual':
                self.tokens.pop(0)
                if self.tokens[0].nombre == 'tk_corA':
                    self.tokens.pop(0)
                    if self.tokens[0].nombre == 'tk_cadena':
                        clave = self.tokens.pop(0)
                        self.listaClaves.append(clave.lexema)
                        self.otraClave()
                        if self.tokens[0].nombre == 'tk_corC':
                            self.tokens.pop(0)
                        else:
                            print("error: se esperaba un corchete de cierre")
                    else:
                        print("error: se esperaba una cadena")
                else:
                    print("Error: se esparaba corchete de apertura")
            else:
                self.recuperar("tk_corA")
                print("error: se esperaba signo igual")
        else:
            self.recuperarDos("tk_igual", "tk_claves")
            print("error: Se esperarba palabra reservada Claves")

    #<otra_clave> ::= tk_coma tk_cadena <otra_clave>
    #               | ε
    def otraClave(self):
        if self.tokens[0].nombre == 'tk_coma':
            self.tokens.pop(0)
            if self.tokens[0].nombre == 'tk_cadena':
                clave = self.tokens.pop(0)
                self.listaClaves.append(clave.lexema)
                self.otraClave()
            else:
                self.recuperarDos("tk_coma", "tk_corC")
                print("error: se esperaba una cadena")
        else:
            pass#Nada porque se acepta épsilon

    #<registros> ::= tk_registros tk_igual tk_corA <registro> <otroRegistro> tk_corC
    def registros(self):
        if self.tokens[0].nombre == 'tk_registros':
            self.tokens.pop(0)
            if self.tokens[0].nombre == 'tk_igual':
                self.tokens.pop(0)
                if self.tokens[0].nombre == 'tk_corA':
                    self.tokens.pop(0)
                    self.registro()
                    self.otroRegistro()
                    if self.tokens[0].nombre == 'tk_corC':
                        self.tokens.pop(0)
                    else:
                        print("error: se esperaba corchete de cierre")
                else:
                    print("error: se esperaba corchete de apertura")
            else:
                print("error: se esperaba signo igual")    
        else:
            print("error: se esperaba la palabra clave Registros")

    #<registro> ::= tk_llaveA <valor> <otroValor> tk_llaveC
    def registro(self):
        if self.tokens[0].nombre == 'tk_llaveA':
            self.tokens.pop(0)
            res = self.valor()
            if res is not None:
                registro = []
                registro.append(res.lexema)
                self.otroValor(registro)
                if self.tokens[0].nombre == 'tk_llaveC':
                    self.tokens.pop(0)
                    self.listaRegistros.append(registro)
                else:
                    print("Error: se esperaba llave de cierre")
        else:
            print("Error: se esperaba llave de apertura")

    #<valor> ::= tk_cadena | tk_entero | tk_decimal
    def valor(self):
        if self.tokens[0].nombre == 'tk_cadena' or self.tokens[0].nombre == 'tk_entero' or self.tokens[0].nombre == 'tk_decimal':
            campo = self.tokens.pop(0)
            return campo
        else:
            print("error: se esperaba una cadena, entero o decimal")
            return None
    
    #<otroValor> ::= tk_coma <valor> <otroValor>
    #              | ε
    def otroValor(self, registro):
        if self.tokens[0].nombre == 'tk_coma':
            self.tokens.pop(0)
            res = self.valor()
            if res is not None:
                registro.append(res.lexema)
                self.otroValor
        else:
            pass#No es error porque aceptamos épsilon

    #<otroRegistro> ::= <registro> <otroRegistro>
    #              | ε
    def otroRegistro(self):
        if self.tokens[0].nombre == 'tk_llaveA':
            self.registro()
            self.otroRegistro()
        else:
            pass#Nada porque aceptamos épsilon
    
    #<funciones> ::= <funcion> <otraFuncion>
    def funciones(self):
        self.funcion()
        self.otraFuncion()

    #<funcion> ::= tk_palabraReservada tk_parA <parametros> tk_parC tk_PyC
    def funcion(self):
        if self.tokens[0].nombre == 'tk_palabraReservada':
            tipo = self.tokens.pop(0)
            if self.tokens[0].nombre == 'tk_parA':
                self.tokens.pop(0)
                parametros = self.parametros()
                if self.tokens[0].nombre == 'tk_parC':
                    self.tokens.pop(0)
                    if self.tokens[0].nombre == 'tk_PyC':
                        self.tokens.pop(0)
                        self.operarFuncion(tipo, parametros)
                    else:
                        print("error: se esperaba punto y coma")
                else:
                    print("error: se esperaba paréntesis de cierre")
            else:
                print("error: se esperaba paréntesis de apertura")
        else:
            print("error: se esperaba palabra reservada de función")

    #<parametros> ::= <valor> <otroParametro>
    #               | ε
    def parametros(self):
        parametros = []
        if self.tokens[0].nombre != 'tk_parC':
            valor = self.valor()
            if valor is not None:
                parametros = [valor]
                self.otroParametro(parametros)
        return parametros

    #<otroParametro> ::= tk_coma <valor> <otroParametro>
    #                  | ε
    def otroParametro(self, parametros):
        if self.tokens[0].nombre == 'tk_coma':
            self.tokens.pop(0)
            valor = self.valor()
            if valor is not None:
                parametros.append(valor)
                self.otroParametro(parametros)

    #<otraFuncion> ::= <funcion> <otraFuncion>
    #                | ε 
    def otraFuncion(self):
        if self.tokens[0].nombre != 'EOF':
            self.funcion()
            self.otraFuncion()
        else:
            print("Análisis terminado")

    #Operación de funciones
    def operarFuncion(self, tipo, parametros):
        if tipo.lexema == 'imprimir':
            if len(parametros) == 1:
                print(parametros[0].lexema)
            else:
                print("error: demasiados parámetros en función imprimir")
                    
        elif tipo.lexema == 'conteo':
            if len(parametros) == 0:
                print(len(self.listaRegistros))
            else:
                print("error: demasiados parámetros en función conteo")
        
        elif tipo.lexema == 'promedio':
            if len(parametros) == 1:
                if parametros[0].nombre == 'tk_cadena':
                    self.promedio(parametros[0].lexema)
                else:
                    print("error: se esperaba una cadena como parámetro en función promedio")
            else:
                print("error: demasiados parámetros en función promedio")

    # Producción <promedio> -> tk_promedio <CadenaFin>
    def promedio(self, campo):
        encontrado = False
        posicion = -1
        for c in self.listaClaves:
            posicion += 1
            if c == campo:
                encontrado = True
                break
        if encontrado:
            suma = 0
            promedio = 0
            for registro in self.listaRegistros:
                if isinstance(registro[posicion], str):
                    suma += len(registro[posicion])
                else:
                    suma += registro[posicion]
            if len(self.listaRegistros) > 0:
                promedio = suma / len(self.listaRegistros)
            print(promedio)