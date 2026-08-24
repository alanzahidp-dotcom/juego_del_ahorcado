# Juego del Ahorcado

## Nombre del proyecto

Juego del Ahorcado en Python

## Integrante

* Alan Paucar

## Objetivo del sistema

Desarrollar un juego del ahorcado utilizando el lenguaje de programación Python, aplicando diferentes conceptos aprendidos durante el curso, como variables, operadores, listas, tuplas, funciones, condicionales, bucles y librerías.

El sistema tiene como objetivo ofrecer un juego interactivo en el que el usuario debe descubrir una palabra seleccionada aleatoriamente antes de quedarse sin intentos. Además, el programa permite volver a jugar y llevar un registro de las partidas ganadas y perdidas.

## Descripción del sistema

El Juego del Ahorcado es un programa desarrollado en Python que permite al usuario intentar descubrir una palabra oculta mediante el ingreso de letras.

Al iniciar el programa se presenta un menú principal con tres opciones:

1. Jugar
2. Estadísticas
3. Salir

Cuando el usuario selecciona la opción de jugar, el sistema selecciona una palabra de manera aleatoria. La palabra se muestra inicialmente mediante guiones bajos y se va descubriendo conforme el usuario ingresa letras correctas.

El jugador cuenta con 6 intentos. Cada letra correcta se incorpora a las letras acertadas, mientras que una letra incorrecta disminuye el número de intentos disponibles. El sistema también evita que el usuario ingrese una letra más de una vez.

La partida termina cuando el jugador descubre completamente la palabra o cuando se terminan los intentos. Al finalizar, el sistema indica si el jugador ganó o perdió y muestra la palabra correcta.

Después de terminar una partida, el usuario puede regresar al menú principal y comenzar una nueva partida.

## Funcionalidades

### Menú principal

El sistema cuenta con un menú que permite:

* Iniciar una partida.
* Consultar las estadísticas.
* Salir del programa.

### Selección aleatoria de palabras

El programa utiliza la librería `random` para seleccionar una palabra de manera aleatoria utilizando `random.choice()`.

### Ingreso de letras

El usuario puede ingresar una letra para intentar descubrir la palabra.

### Validación de datos

El sistema verifica que:

* Se ingrese solamente una letra.
* No se ingresen números o símbolos.
* La letra no haya sido utilizada anteriormente.

### Control de intentos

El jugador comienza con 6 intentos. Cada vez que introduce una letra incorrecta, pierde un intento.

### Visualización del progreso

Las letras acertadas se muestran en la posición correspondiente de la palabra, mientras que las letras que todavía no han sido descubiertas se representan mediante `_`.

### Sistema de victoria y derrota

El jugador gana cuando descubre todas las letras de la palabra.

El jugador pierde cuando sus intentos llegan a cero.

### Estadísticas

El sistema registra:

* Partidas jugadas.
* Partidas ganadas.
* Partidas perdidas.

Las estadísticas pueden consultarse desde el menú principal.

### Repetición de partidas

Después de terminar una partida, el usuario puede regresar al menú y jugar nuevamente sin cerrar el programa.

## Conceptos de Python utilizados

El proyecto aplica diferentes elementos fundamentales del lenguaje Python.

### Variables

Se utilizan variables para almacenar información como:

* Palabra seleccionada.
* Intentos restantes.
* Letras acertadas.
* Letras utilizadas.
* Partidas ganadas.
* Partidas perdidas.

### Tuplas

Se utiliza una tupla para almacenar las palabras disponibles:

```python
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
```

La tupla permite mantener un conjunto de palabras que no necesita modificarse durante la ejecución.

### Listas

Se utilizan listas para almacenar las letras que el jugador ha utilizado y las letras que ha acertado.

```python
letras_acertadas = []
letras_usadas = []
```

También se utiliza el método `append()` para agregar nuevas letras a estas listas.

### Funciones

El programa está dividido en diferentes funciones para organizar mejor el código:

* `mostrar_menu()`
* `elegir_palabra()`
* `mostrar_palabra()`
* `validar_letra()`
* `jugar()`
* `mostrar_estadisticas()`

La separación en funciones permite organizar la lógica del programa y facilita su mantenimiento.

### Condicionales

Se utilizan estructuras `if`, `elif` y `else` para tomar decisiones.

Por ejemplo, se utilizan para comprobar:

* Si una letra pertenece a la palabra.
* Si una letra ya fue utilizada.
* Si el jugador ganó.
* Si el jugador perdió.
* Qué opción seleccionó en el menú.

### Bucles

Se utilizan dos tipos principales de bucles.

#### `while`

Se utiliza para mantener activo el menú principal y para controlar los intentos durante una partida.

#### `for`

Se utiliza para recorrer las letras de la palabra y determinar cuáles deben mostrarse y cuáles deben permanecer ocultas.

### Librería `random`

Se utiliza la librería `random` para seleccionar una palabra de forma aleatoria.

```python
import random
```

Y posteriormente:

```python
random.choice(palabras)
```

### Entrada y salida de datos

Se utiliza `input()` para recibir información del usuario y `print()` para mostrar información en pantalla.

### Operadores

El programa utiliza operadores de comparación, lógicos y de asignación para realizar las diferentes comprobaciones y operaciones.

Entre ellos:

* `==`
* `!=`
* `>`
* `<=`
* `+=`
* `-=`
* `in`
* `not`

### Retorno de valores

Las funciones utilizan `return` para devolver información al programa principal.

Por ejemplo, la función `jugar()` devuelve:

```python
True
```

cuando el jugador gana y:

```python
False
```

cuando pierde.

Esto permite actualizar correctamente las estadísticas.

## Estructura del proyecto

El proyecto se encuentra dividido en dos archivos principales:

```text
AHORCADO/
│
├── cod_completo.py
└── funciones.py
```

### `cod_completo.py`

Es el archivo principal del programa. Se encarga de:

* Importar las funciones.
* Contener las palabras disponibles.
* Inicializar las estadísticas.
* Mostrar y controlar el menú.
* Iniciar las partidas.
* Actualizar las victorias y derrotas.
* Finalizar el programa.

### `funciones.py`

Contiene las funciones utilizadas por el programa:

* `mostrar_menu()`
* `elegir_palabra()`
* `mostrar_palabra()`
* `validar_letra()`
* `jugar()`
* `mostrar_estadisticas()`

La separación permite mantener el código organizado y facilita la reutilización de las funciones.

## Arquitectura del sistema

La arquitectura básica del proyecto funciona de la siguiente manera:

```text
                         USUARIO
                            │
                            ↓
                  ┌─────────────────┐
                  │ cod_completo.py │
                  │                 │
                  │ Programa        │
                  │ principal       │
                  └────────┬────────┘
                           │
                           │ utiliza
                           ↓
                  ┌─────────────────┐
                  │   funciones.py  │
                  │                 │
                  │ Lógica del juego│
                  └────────┬────────┘
                           │
                           ↓
                  ┌─────────────────┐
                  │     random      │
                  │                 │
                  │ Selección       │
                  │ aleatoria       │
                  └─────────────────┘
```

## Flujo general del sistema

El funcionamiento general del programa es:

```text
Inicio
  ↓
Mostrar menú
  ↓
Seleccionar opción
  ↓
┌────────────┬───────────────┬────────────┐
│   JUGAR    │ ESTADÍSTICAS  │   SALIR    │
└─────┬──────┴───────┬───────┴─────┬──────┘
      ↓              ↓             ↓
  Iniciar partida  Mostrar      Finalizar
      ↓           estadísticas   programa
  Actualizar          ↓
  estadísticas        │
      ↓               │
      └───────┬───────┘
              ↓
        Volver al menú
```

## Requisitos

Para ejecutar el proyecto se necesita:

* Python 3.
* Un editor de código o entorno compatible con Python.
* Los archivos `cod_completo.py` y `funciones.py` dentro de la misma carpeta.

No es necesario instalar librerías externas, ya que `random` forma parte de la biblioteca estándar de Python.

## Ejecución

Para ejecutar el programa se debe abrir el archivo:

```text
cod_completo.py
```

Al iniciar, aparecerá el menú principal:

```text
================================
       JUEGO DEL AHORCADO
================================
1. JUGAR
2. ESTADÍSTICAS
3. SALIR
================================
```

El usuario debe seleccionar una de las opciones disponibles.

## Fecha

23 de agosto de 2026
