import math

alturas = [1.92, 1.80, 1.90, 1.89, 1.70, 1.67, 1.74, 1.75, 1.69, 1.69, 1.85, 1.72, 1.70, 1.86, 1.68, 1.74, 1.70, 1.75]
pesos = [70, 85, 75, 72, 60, 65, 66, 85, 64, 67, 90, 65, 95, 74, 68, 90, 80, 70]


def calc_media(values: list) -> float:
    media = 0
    for value in values:
        media += value
    media = media / len(values)

    return media


def calc_varianza(values: list) -> float:
    n = len(values)
    m = calc_media(values)
    var = 0

    for value in values:
        var += (value - m)**2

    var = var / n

    return var


def check_option(option: str) -> bool:
    if not option.isdigit():
        print("Opcion no valida.")
        input("\n\n\nEnter para continuar")
        return False
    option = int(option)
    if not option >= 0 and option < 3:
        return False
    return True


def calc_desviacion(values: list) -> float:
    var = calc_varianza(values)

    return math.sqrt(var)


def varianza():
    options = "CALCULAR VARIANZA".center(50, "=") + "\n" + \
              " - (1) Calcular varianza de las alturas\n" + \
              " - (2) Calcular varianza de los pesos\n" + \
              " - (0) Salir\n"

    while True:
        print(options)
        option = input("\nOpcion: ")

        if not check_option(option):
            continue

        option = int(option)

        if option == 0:
            break
        elif option == 1:
            var = calc_varianza(alturas)
            print("El valor de la varianza de las alturas es", var)
        elif option == 2:
            var = calc_varianza(pesos)
            print("El valor de la varianza de los pesos es", var)

        input("\n\n\nEnter to continue")


def desviacion():
    options = ("CALCULAR DESVIACION".center(50, "=") + "\n" +
               " - (1) Calcular desviacion de las alturas" + "\n" +
               " - (2) Calcular desviacion de los pesos" + "\n" +
               " - (0) Salir\n" +
               ("=" * 50))

    while True:
        print(options)
        option = input("\nOpcion: ")

        if not check_option(option):
            continue

        option = int(option)

        if option == 0:
            break
        elif option == 1:
            var = calc_desviacion(alturas)
            print("El valor de la desviacion de las alturas es", var)
        elif option == 2:
            var = calc_desviacion(pesos)
            print("El valor de la desviacion de los pesos es", var)

        input("\n\n\nEnter to continue")


def media():
    options = ("CALCULAR MEDIA".center(50, "=") + "\n" +
               " - (1) Calcular media de las alturas" + "\n" +
               " - (2) Calcular media de los pesos" + "\n" +
               " - (0) Salir\n" +
               ("=" * 50))

    while True:
        print(options)
        option = str(input("\nOpcion: "))

        if not check_option(option):
            continue

        option = int(option)

        if option == 0:
            break
        elif option == 1:
            value = calc_media(alturas)
            print("El valor de la media de las alturas es", value)
        elif option == 2:
            value = calc_media(pesos)
            print("El valor de la media de los pesos es", value)

        input("\n\n\nEnter to continue")
