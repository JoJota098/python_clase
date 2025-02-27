palabra = input("Ingresa la palabra a buscar: ").lower()
contador = 0

with open("./basicos/archivos/articulo.txt", "r") as archivo:
    for linea in archivo:
        palabras_linea = linea.lower().split()
        contador += palabras_linea.count(palabra)

print(f"La palabra '{palabra}' aparece {contador} veces.")