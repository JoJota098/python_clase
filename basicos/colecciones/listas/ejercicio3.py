#usando apend
numeros = [10, 20, 30]

numeros.append(40)  
numeros.append(50)   
numeros.append(60)   

print(numeros) 

#usando extend
numeros = [10, 20, 30]
nuevos_elementos = [40, 50, 60]

numeros.extend(nuevos_elementos)
print(numeros)  

#usando operador + concatenar
numeros = [10, 20, 30]
numeros += [40, 50, 60] 
print(numeros)

#usando insert
numeros = [10, 20, 30]

numeros.insert(0, 5)    # Inserta 5 en la posicion 0
numeros.insert(2, 25)   # Inserta 25 en la posicion 2
numeros.insert(4, 35)   # Inserta 35 en la posicion 4

print(numeros)