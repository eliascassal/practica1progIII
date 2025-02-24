import random

def generar_numeros_aleatorios():
    # Solicitar al usuario el rango de números
    rango_inferior = int(input("Ingrese el límite inferior del rango: "))
    rango_superior = int(input("Ingrese el límite superior del rango: "))
    cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))

    # Generar números aleatorios dentro del rango
    lista_numeros_aleatorios = [random.randint(rango_inferior, rango_superior) for _ in range(cantidad_numeros)]

    # Mostrar la lista de números aleatorios al usuario
    print("Lista de números aleatorios generados:", lista_numeros_aleatorios)

# Llamar a la función para generar los números aleatorios
generar_numeros_aleatorios()
