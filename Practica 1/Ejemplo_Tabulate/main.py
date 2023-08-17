# Para instalar el módulo "tabulate"
# Abren una consola y colocan:
#           pip install tabulate
# Luego ya pueden importarlo como a continuación

from tabulate import tabulate #Se importa el módulo instalado


#Esta tabla deberían construirla al recorrer sus listas/diccionarios/lo_que_hayan_usado
tabla = [
            ["Tomates", 100, 1.00, 100.00, "BodegaA"], # Cada una de estas es una fila
            ["Arándanos", 155, 0.50, 77.50, "BodegaA"], # Fila
            ["Helado", 80, 6.50, 520.00, "BodegaB"],    # Fila
            ["Peras", 175, 3.25, 568.75, "BodegaC"]     # Fila
        ]

# Headers son los títulos de la tabla, en este caso puedo símplemente copiarlo como está
# porque siempre van a ser los mismos
print(tabulate(tabla, headers=["Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"]))