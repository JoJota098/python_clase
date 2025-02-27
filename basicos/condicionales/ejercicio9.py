# input temp
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# if temperaturas
if celsius >= 30:
    print("Hace calor.")
elif 10 <= celsius < 30:
    print("El clima es templado.")
else:
    print("Hace frío.")