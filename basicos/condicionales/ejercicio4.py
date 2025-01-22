num1 = int(input("Dame el primer numero"))
num2 = int(input("Dame el segundo numero"))

if num1 > num2:
    print(f"El primer número {num1} es mayor")
elif num2 > num1:
    print(f"El segundo numero {num2} es mayor")
elif num1 == num2:
    print(f"Los numeros son iguales")