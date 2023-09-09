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

if __name__ == '__main__':
    txt = abrir()
    if txt is not None:
        lexer = Analizador(txt)
        lexer.analizar()
        print("--------------------------- Tokens ---------------------------")
        for i in lexer.tokens_reconocidos:
            print(i)
        print("--------------------------- Errores ---------------------------")
        for i in lexer.errores:
            print(i)
    else:
        print(":(")