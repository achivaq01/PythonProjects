alturas = [1.92, 1.80, 1.90, 1.89, 1.70, 1.67, 1.74, 1.75, 1.69, 1.69, 1.85, 1.72, 1.70, 1.86, 1.68, 1.74, 1.70, 1.75]
pesos = [70, 85, 75, 72, 60, 65, 66, 85, 64, 67, 90, 65, 95, 74, 68, 90, 80, 70]


def check_option(option: str) -> bool:
    if not option.isdigit():
        print("Opcion no valida.")
        input("\n\n\nEnter para continuar")
        return False
    option = int(option)
    if not option >= 0 and option < 3:
        return False
    return True