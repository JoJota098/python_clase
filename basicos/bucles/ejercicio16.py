contrasena_correcta = "python123"

while True:
    contrasena_usuario = input("Dame una contraseña")
    if contrasena_correcta == contraseña_usuario:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")