productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
valor = 1.0
productos_filtrados = []

for producto in productos:
    if productos[producto] > valor:
        productos_filtrados.append(producto)

print(productos_filtrados)
