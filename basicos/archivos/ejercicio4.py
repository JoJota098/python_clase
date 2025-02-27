nombres = ["Ana", "Luis", "Marta", "Carlos"]

with open("./basicos/archivos/nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")