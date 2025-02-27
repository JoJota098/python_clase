with open("./basicos/archivos/poema.txt", "r") as archivo:
    lineas = archivo.readlines()
print(f"El archivo tiene {len(lineas)} líneas.")