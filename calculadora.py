def sumar(a, b):
    return a + b

// resta de 2 valores
def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))


    print("Resultado de la suma:", sumar(numero1, numero2))
    print("Resultado de la resta:", restar(numero1, numero2))
    print("Resultado de la multiplicación:", multiplicar(numero1, numero2))

    try:
        print("Resultado de la división:", dividir(numero1, numero2))
    except ValueError as e:
        print("Resultado de la división:", e)


if __name__ == "__main__":
    main()
