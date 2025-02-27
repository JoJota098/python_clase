# definir conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# usando intersection()
interseccion_1 = conjunto_a.intersection(conjunto_b)

# usando operador &
interseccion_2 = conjunto_a & conjunto_b

# print resultado
print(interseccion_1)  # Salida: {2, 3}
print(interseccion_2)  # Salida: {2, 3}