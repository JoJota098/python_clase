import random

while True:
    numero = random.randint(1, 10)
    print(f"Número generado: {numero}")
    if numero > 8:
        print("¡Número mayor que 8!")
        break