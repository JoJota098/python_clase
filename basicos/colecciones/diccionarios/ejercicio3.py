#usando del
diccionario = {
    "nombre": "Juan",
    "edad": 21,
    "ciudad": "Madrid"
}

del diccionario["edad"]

print(diccionario)

#usando pop
diccionario = {
    "nombre": "Juan",
    "edad": 21,
    "ciudad": "Madrid"
}

valor_eliminado = diccionario.pop("edad")

print("Diccionario actualizado:", diccionario)
print("Valor eliminado:", valor_eliminado)