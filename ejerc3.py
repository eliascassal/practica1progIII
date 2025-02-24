def conversor_unidades():
    """Convierte unidades de longitud o temperatura."""

    print("Conversor de Unidades")
    print("--------------------")

    while True:
        print("Opciones de conversión:")
        print("1. Longitud")
        print("2. Temperatura")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '3':
            break

        if opcion == '1':
            convertir_longitud()
        elif opcion == '2':
            convertir_temperatura()
        else:
            print("Opción inválida.")

def convertir_longitud():
    """Convierte unidades de longitud."""

    print("\nConversión de Longitud")
    print("---------------------")

    print("Unidades disponibles:")
    print("1. Metros a Centímetros")
    print("2. Kilómetros a Metros")
    print("3. Centímetros a Metros")
    print("4. Metros a Kilómetros")

    opcion = input("Selecciona una opción (1-4): ")

    try:
        cantidad = float(input("Ingresa la cantidad a convertir: "))

        if opcion == '1':
            resultado = cantidad * 100
            unidad_destino = "centímetros"
        elif opcion == '2':
            resultado = cantidad * 1000
            unidad_destino = "metros"
        elif opcion == '3':
            resultado = cantidad / 100
            unidad_destino = "metros"
        elif opcion == '4':
            resultado = cantidad / 1000
            unidad_destino = "kilómetros"
        else:
            print("Opción inválida.")
            return

        print(f"{cantidad} {obtener_unidad(opcion, 'longitud')} son {resultado} {unidad_destino}.")

    except ValueError:
        print("Cantidad inválida. Ingresa un número.")

def convertir_temperatura():
    """Convierte unidades de temperatura."""

    print("\nConversión de Temperatura")
    print("------------------------")

    print("Unidades disponibles:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

    opcion = input("Selecciona una opción (1-2): ")

    try:
        cantidad = float(input("Ingresa la cantidad a convertir: "))

        if opcion == '1':
            resultado = (cantidad * 9/5) + 32
            unidad_destino = "Fahrenheit"
        elif opcion == '2':
            resultado = (cantidad - 32) * 5/9
            unidad_destino = "Celsius"
        else:
            print("Opción inválida.")
            return

        print(f"{cantidad} {obtener_unidad(opcion, 'temperatura')} son {resultado} {unidad_destino}.")

    except ValueError:
        print("Cantidad inválida. Ingresa un número.")

def obtener_unidad(opcion, tipo):
    """Obtiene la unidad correspondiente a la opción seleccionada."""

    if tipo == 'longitud':
        unidades = ["metros", "kilómetros", "centímetros", "metros"]
    elif tipo == 'temperatura':
        unidades = ["Celsius", "Fahrenheit"]
    else:
        return ""

    return unidades[int(opcion) - 1]

conversor_unidades()