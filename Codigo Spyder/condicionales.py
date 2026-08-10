# ==========================================
#       JUEGO DEL AHORCADO
#       SOLO CONDICIONALES
# ==========================================


# Definimos la palabra secreta
palabra = "python"

# Definimos la cantidad de intentos
intentos = 6


# Pedimos una letra al jugador
letra = input("Ingresa una letra: ").lower()


# Comprobamos si la letra está en la palabra

if letra in palabra:

    print("¡Correcto! La letra está en la palabra.")

else:

    print("Incorrecto. La letra no está en la palabra.")

    # Restamos un intento
    intentos = intentos - 1


# Comprobamos si todavía quedan intentos

if intentos > 0:

    print("Todavía tienes", intentos, "intentos.")

else:

    print("¡Perdiste!")
    print("La palabra era:", palabra)