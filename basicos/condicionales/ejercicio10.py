#input precio
precio = float(input("Ingresa el precio del producto: "))

if precio > 1000:
    descuento = precio * 0.10
    precio_final = precio - descuento
else:
    precio_final = precio

# print final
print(f"Precio final: ${precio_final:.2f}") # :.2f muestra dos decimales 