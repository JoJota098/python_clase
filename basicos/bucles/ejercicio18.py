import random

secreto = random.randint(1, 20)
print("Adivina el número (1-20) o escribe 'salir'.")

while True:
    entrada = input("Tu intento: ")
    if entrada.lower() == "salir":
        print("¡Hasta luego!")
        break
    try:
        intento = int(entrada)
        if intento == secreto:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto. Sigue intentando.")
    except ValueError:
        print("Entrada inválida.")