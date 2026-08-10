# ==========================================
#          JUEGO DEL AHORCADO
# ==========================================


# ---------- ETAPA 1: INICIALIZACIÓN ----------

# Definimos la palabra secreta
palabra = "python"

# Definimos la cantidad de intentos
intentos = 6

# Creamos una lista para guardar las letras acertadas
letras_acertadas = []


# ---------- ETAPA 2: INICIO DEL JUEGO ----------

# Repetimos el juego mientras no haya un ganador o perdedor
while True:

    # ---------- MOSTRAR ESTADO DEL JUEGO ----------

    # Creamos una variable para mostrar la palabra oculta
    palabra_mostrada = ""

    # Revisamos cada letra de la palabra
    for letra in palabra:

        # Si la letra ya fue acertada, la mostramos
        if letra in letras_acertadas:
            palabra_mostrada += letra + " "

        # Si todavía no fue acertada, mostramos "_"
        else:
            palabra_mostrada += "_ "

    # Mostramos la palabra y los intentos restantes
    print("\nPalabra:", palabra_mostrada)
    print("Intentos restantes:", intentos)


    # ---------- CONDICIÓN: ¿QUEDAN INTENTOS? ----------

    # Si los intentos llegaron a cero, el jugador pierde
    if intentos == 0:

        print("\n¡PERDISTE!")
        print("La palabra era:", palabra)

        # Terminamos el juego
        break


    # ---------- ETAPA 3: INGRESAR UNA LETRA ----------

    # Pedimos al jugador que ingrese una letra
    letra = input("Ingresa una letra: ").lower()


    # ---------- CONDICIÓN: ¿LA ENTRADA ES VÁLIDA? ----------

    # Comprobamos que haya ingresado solamente una letra
    if len(letra) != 1 or not letra.isalpha():

        # Mostramos un mensaje de error
        print("Entrada no válida. Ingresa solamente una letra.")

        # Volvemos al inicio del ciclo para pedir otra letra
        continue


    # ---------- ETAPA 4: COMPROBAR LA LETRA ----------

    # Comprobamos si la letra está dentro de la palabra
    if letra in palabra:

        # La letra es correcta
        print("¡Correcto! La letra está en la palabra.")

        # Comprobamos que no haya sido ingresada anteriormente
        if letra not in letras_acertadas:

            # Guardamos la letra acertada
            letras_acertadas.append(letra)


    # Si la letra no está en la palabra
    else:

        # Mostramos un mensaje de error
        print("Incorrecto. La letra no está en la palabra.")

        # Restamos un intento
        intentos = intentos - 1


    # ---------- ETAPA 5: COMPROBAR SI GANÓ ----------

    # Suponemos inicialmente que la palabra está completa
    palabra_completa = True

    # Revisamos todas las letras de la palabra
    for letra in palabra:

        # Si encontramos una letra que todavía no fue acertada
        if letra not in letras_acertadas:

            # La palabra todavía no está completa
            palabra_completa = False


    # Si todas las letras fueron acertadas, el jugador gana
    if palabra_completa:

        print("\n¡GANASTE! 🏆")
        print("La palabra era:", palabra)

        # Terminamos el juego
        break
