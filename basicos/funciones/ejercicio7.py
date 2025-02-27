def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


imprimir_detalles(nombre="Ana", edad=30)

print('-------------------------------------')

imprimir_detalles(producto="Manzana", precio=1.5)
