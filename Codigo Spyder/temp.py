# JUEGO DEL AHORCADO

palabra = "python"
intentos = 6
letras_acertadas = []

while True:

    # Mostrar palabra oculta
    palabra_mostrada = ""

    for letra in palabra:
        if letra in letras_acertadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    print("\nPalabra:", palabra_mostrada)
    print("Intentos restantes:", intentos)

    if intentos == 0:
        print("\n¡PERDISTE!")
        print("La palabra era:", palabra)
        break

    letra = input("Ingresa una letra: ").lower()


    # ¿La entrada es válida?

    if len(letra) != 1 or not letra.isalpha():
        print("Entrada no válida. Ingresa solamente una letra.")
        continue

    if letra in palabra:

        print("¡Correcto! La letra está en la palabra.")

        if letra not in letras_acertadas:
            letras_acertadas.append(letra)

    else:

        print("Incorrecto. La letra no está en la palabra.")
        intentos = intentos - 1

    palabra_completa = True

    for letra in palabra:
        if letra not in letras_acertadas:
            palabra_completa = False

    if palabra_completa:
        print("\n¡GANASTE! 🏆")
        print("La palabra era:", palabra)
        break