options = ("CALCULAR MEDIA".center(50, "=") + "\n" +
           " - 1) Calcular media de las alturas" + "\n" +
           " - 2) Calcular media de los pesos" + "\n" +
           " - 0) Salir\n" +
           ("=" * 50))
alturas = [1.92, 1.80, 1.90, 1.89, 1.70, 1.67, 1.74, 1.75, 1.69, 1.69, 1.85, 1.72, 1.70, 1.86, 1.68, 1.74, 1.70, 1.75]
pesos = [70, 85, 75, 72, 60, 65, 66, 85, 64, 67, 90, 65, 95, 74, 68, 90, 80, 70]

def check_option(option: str) -> bool:
    if not option.isdigit():
        return False
    option = int(option)
    if not option >= 0 and option < 3:
        return False
    return True

def calc_media(values: list) -> float:
    media = 0
    for value in values:
        media += value
    media = media / len(values)

    return media


flg_0 = True
flg_1 = False
flg_2 = False

while flg_0:
    print(options)
    option = str(input("\nOpcion: "))

    if not check_option(option):
        print("Opcion no valida.")
        input("Enter para continuar\n\n\n")
        continue

    option = int(option)

    if option == 0:
        flg_0 = False
    elif option == 1:
        value = calc_media(alturas)
        print("El valor de la media de las alturas es", value)
        input("Enter to continue\n\n\n")
    else:
        value = calc_media(pesos)
        print("El valor de la media de los pesos es", value)
        input("Enter to continue\n\n\n")









