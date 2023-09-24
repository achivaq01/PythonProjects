from functions import *

options = ("CALCULADORA ESTADISTICA".center(50, "=") + "\n" +
           " - (1) Calcular media" + "\n" +
           " - (2) Calcular varianza" + "\n" +
           " - (3) Calcular desviacion\n" +
           " - (0) Salir\n" + ("=" * 50))

while True:
    print(options)
    option = input("\nOpcion: ")

    if not check_option(option):
        continue

    option = int(option)

    if option == 0:
        break
    elif option == 1:
        media()
    elif option == 2:
        varianza()
    elif option == 3:
        desviacion()

    input("\n\n\nEnter to continue")