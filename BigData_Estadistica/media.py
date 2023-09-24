import main

options = ("CALCULAR MEDIA".center(50, "=") + "\n" +
           " - (1) Calcular media de las alturas" + "\n" +
           " - (2) Calcular media de los pesos" + "\n" +
           " - (0) Salir\n" +
           ("=" * 50))


def calc_media(values: list) -> float:
    media = 0
    for value in values:
        media += value
    media = media / len(values)

    return media


while True:
    print(options)
    option = str(input("\nOpcion: "))

    if not main.check_option(option):
        continue

    option = int(option)

    if option == 0:
        break
    elif option == 1:
        value = calc_media(main.alturas)
        print("El valor de la media de las alturas es", value)
    elif option == 2:
        value = calc_media(main.pesos)
        print("El valor de la media de los pesos es", value)

    input("\n\n\nEnter to continue")
