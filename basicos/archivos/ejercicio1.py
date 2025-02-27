import os

# Imprime el directorio actual desde donde se ejecuta el script
print("Directorio actual:", os.getcwd())

# Lista los archivos en el directorio actual
print("Archivos en el directorio:", os.listdir())


#'''

with open("./basicos/archivos/notas.txt", "r") as archivo:
    contenido = archivo.read()
print(contenido)

#'''