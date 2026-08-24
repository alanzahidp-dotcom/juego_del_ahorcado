
from funciones import (
    mostrar_menu,
    jugar,
    mostrar_estadisticas
)


# Lista de palabras disponibles para el juego
palabras = (
    "python",
    "computadora",
    "teclado",
    "programacion",
    "internet",
    "algoritmo",
    "variable",
    "funcion",
    "programador",
    "codigo"
)


# Contadores de partidas
ganadas = 0
perdidas = 0


# Programa principal
while True:

    mostrar_menu()

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":

        resultado = jugar(palabras)

        if resultado:
            ganadas += 1
        else:
            perdidas += 1

        input("\nPresiona ENTER para volver al menú...")

    elif opcion == "2":

        mostrar_estadisticas(ganadas, perdidas)

        input("\nPresiona ENTER para volver al menú...")

    elif opcion == "3":

        print("\n================================")
        print("      ¡GRACIAS POR JUGAR!")
        print("================================")
        print(f"Partidas ganadas: {ganadas}")
        print(f"Partidas perdidas: {perdidas}")
        print("Programa finalizado.")

        break

    else:

        print("\nOpción no válida.")
        print("Selecciona 1, 2 o 3.")

