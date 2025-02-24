import random

def juego_adivinanza():
    """Juego donde el usuario adivina un número aleatorio."""

    print("¡Bienvenido al juego de adivinanza!")
    print("----------------------------------")

    numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos = 0

    while True:
        try:
            intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
            continue

        intentos += 1

        if intento_usuario == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento_usuario < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

juego_adivinanza()