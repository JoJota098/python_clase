with open("./basicos/archivos/origen.txt", "r") as origen:
    contenido = origen.read()

with open("./basicos/archivos/destino.txt", "w") as destino:
    destino.write(contenido)