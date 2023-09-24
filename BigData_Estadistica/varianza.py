import main
import media


def calcular_varianza(values: list) -> float:
    n = len(values)
    m = media.calc_media(values)
    var = 0

    for value in values:
        var += (value - m)**2

    var = var / n

    return var


options = "CALCULAR VARIANZA".center(50, "=") + "\n" + \
          " - (1) Calcular varianza de las alturas\n" + \
          " - (2) Calcular varianza de los pesos\n" + \
          " - (0) Salir\n"

while True:
    print(options)
    option = input("\nOpcion: ")

    if not main.check_option(option):
        continue

    option = int(option)

    if option == 0:
        break
    elif option == 1:
        var = calcular_varianza(main.alturas)
        print("El valor de la varianza de las alturas es", var)
    elif option == 2:
        var = calcular_varianza(main.pesos)
        print("El valor de la varianza de los pesos es", var)

    input("\n\n\nEnter to continue")


