import math

def calcular_area_perimetro():
    """Calcula el área y perímetro de una figura geométrica."""

    print("Calculadora de Área y Perímetro")
    print("-----------------------------")

    while True:
        print("Figuras disponibles:")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Salir")

        opcion = input("Selecciona una figura (1-4): ")

        if opcion == '4':
            break

        try:
            if opcion == '1':
                lado = float(input("Ingresa el lado del cuadrado: "))
                area = lado ** 2
                perimetro = 4 * lado
            elif opcion == '2':
                base = float(input("Ingresa la base del rectángulo: "))
                altura = float(input("Ingresa la altura del rectángulo: "))
                area = base * altura
                perimetro = 2 * (base + altura)
            elif opcion == '3':
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                lado1 = float(input("Ingresa el primer lado del triángulo: "))
                lado2 = float(input("Ingresa el segundo lado del triángulo: "))
                area = (base * altura) / 2
                perimetro = base + lado1 + lado2
            else:
                print("Opción inválida.")
                continue

            print("Resultados:")
            print(f"Área: {area}")
            print(f"Perímetro: {perimetro}")

        except ValueError:
            print("Dimensiones inválidas. Ingresa números.")

calcular_area_perimetro()