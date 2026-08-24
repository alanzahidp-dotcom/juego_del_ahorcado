import random


def mostrar_menu():
    print("\n================================")
    print("       JUEGO DEL AHORCADO")
    print("================================")
    print("1. JUGAR")
    print("2. ESTADÍSTICAS")
    print("3. SALIR")
    print("================================")


def elegir_palabra(palabras):
    return random.choice(palabras)


def mostrar_palabra(palabra, letras_acertadas):
    resultado = ""

    for letra in palabra:
        if letra in letras_acertadas:
            resultado += letra + " "
        else:
            resultado += "_ "

    return resultado


def validar_letra(letras_usadas):
    while True:
        letra = input("Ingresa una letra: ").lower().strip()

        if len(letra) != 1:
            print("Debes ingresar solamente una letra.")

        elif not letra.isalpha():
            print("Debes ingresar una letra, no un número o símbolo.")

        elif letra in letras_usadas:
            print("Ya utilizaste esa letra. Intenta con otra.")

        else:
            return letra


def jugar(palabras):
    palabra = elegir_palabra(palabras)

    letras_acertadas = []
    letras_usadas = []
    intentos = 6

    print("\n================================")
    print("        COMIENZA EL JUEGO")
    print("================================")

    while intentos > 0:

        print("\nPalabra:", mostrar_palabra(palabra, letras_acertadas))
        print("Letras utilizadas:", letras_usadas)
        print("Intentos restantes:", intentos)

        letra = validar_letra(letras_usadas)
        letras_usadas.append(letra)

        if letra in palabra:
            letras_acertadas.append(letra)
            print("¡Correcto! La letra está en la palabra.")

            if "_" not in mostrar_palabra(palabra, letras_acertadas):
                print("\n¡FELICIDADES! Has ganado.")
                print(f"La palabra era: {palabra}")
                return True

        else:
            intentos -= 1
            print("Incorrecto. La letra no está en la palabra.")

    print("\nHas perdido.")
    print(f"La palabra era: {palabra}")

    return False


def mostrar_estadisticas(ganadas, perdidas):
    jugadas = ganadas + perdidas

    print("\n================================")
    print("          ESTADÍSTICAS")
    print("================================")
    print(f"Partidas jugadas: {jugadas}")
    print(f"Partidas ganadas: {ganadas}")
    print(f"Partidas perdidas: {perdidas}")
    print("================================")