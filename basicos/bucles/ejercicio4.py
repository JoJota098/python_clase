cadena = "Python es maravilloso"

count = 0
vocales = "aeiouAEIOU"
for caracter in cadena:
    if caracter in vocales:
        count += 1
print(f"La cadena tiene {count} vocales")