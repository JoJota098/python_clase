cadena = "Python es genial"
vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
contador = 0

for letra in cadena:
    if letra in vocales:
        contador += 1

print(f"Vocales: {contador}")  