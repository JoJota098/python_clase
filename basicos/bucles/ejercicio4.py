'''cadena = "Python es maravilloso"

count = 0
vocales = "aeiouAEIOU"
for caracter in cadena:
    if caracter in vocales:
        count += 1
print(f"La cadena tiene {count} vocales")'''

productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}") #poner 2 decimales