def main():
    saludo()
    saludar('Luis',20)
    print(suma(3,14))
    sumar_varios(3,4,5,6,7,89,23,10)

def saludo():
    print(f'Hola Mundo!')


def saludar(nombre,edad):
    print(f'Hola Mr. {nombre} tienes {edad} años')


def saludoPideNombre():
    nombre=input('Dame un nombre: ')
    print(f'Hola {nombre} ¿Que tal?')

def suma(num1, num2):
    total = num1+num2
    return total


def sumar_varios(*args):
    print('Voy a sumar los numeros')

    for n in args:
        print(n)
    
    total = sum(args)
    print(f'El total es: {total}')



if __name__ == '__main__':
    main()
