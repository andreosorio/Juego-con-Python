
# =====================================================
# PROYECTO: JUEGO DEL AHORCADO
# ESTRUCTURAS DE DATOS Y ALGORITMOS EN PYTHON
# =====================================================


# =====================================================
# PARTE 1: LISTAS LIGADAS Y COLAS
# =====================================================

# Creacion de un nodo para la lista ligada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Creacion de la lista ligada
class ListaLigada:
    def __init__(self):
        self.inicio = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.inicio is None:
            self.inicio = nuevo
        else:
            actual = self.inicio

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.inicio

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("Fin")


# Creacion de una cola (Queue)
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


# =====================================================
# PARTE 2: PILAS Y DIBUJO DEL AHORCADO
# =====================================================

# Creacion de una pila (Stack)
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        return None

    def cantidad(self):
        return len(self.elementos)

    def mostrar(self):
        print(self.elementos)


# Dibujos del ahorcado segun los errores
dibujos = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


# Funcion para mostrar el dibujo
def mostrar_ahorcado(errores):
    print(dibujos[errores])


# =====================================================
# PARTE 3: ALGORITMOS DE BUSQUEDA Y ORDENAMIENTO
# =====================================================

# Busqueda secuencial de jugadores
def buscar_jugador(jugadores, nombre):

    for jugador in jugadores:

        if jugador["nombre"].lower() == nombre.lower():
            return jugador

    return None


# Algoritmo de ordenamiento burbuja
def ordenar_jugadores(jugadores):

    n = len(jugadores)

    for i in range(n):

        for j in range(0, n - i - 1):

            if jugadores[j]["puntos"] < jugadores[j + 1]["puntos"]:

                temporal = jugadores[j]

                jugadores[j] = jugadores[j + 1]

                jugadores[j + 1] = temporal

    return jugadores


# Mostrar clasificacion
def mostrar_clasificacion(jugadores):

    print("\n================================")
    print("       TABLA DE POSICIONES")
    print("================================")

    for posicion, jugador in enumerate(jugadores, start=1):

        print(
            posicion,
            "-",
            jugador["nombre"],
            "| Puntos:",
            jugador["puntos"]
        )


# =====================================================
# PARTE 4: LOGICA PRINCIPAL DEL JUEGO
# =====================================================

def jugar_palabra(palabra, jugador):

    palabra = palabra.upper()

    letras_usadas = []

    errores = Pila()

    historial = ListaLigada()

    puntos = 0

    print("\n================================")
    print("       JUEGO DEL AHORCADO")
    print("================================")

    print("Jugador:", jugador)

    # Ciclo principal de la partida
    while errores.cantidad() < 6:

        mostrar_ahorcado(errores.cantidad())

        # Mostrar palabra oculta
        palabra_oculta = ""

        for letra in palabra:

            if letra in letras_usadas:
                palabra_oculta += letra + " "
            else:
                palabra_oculta += "_ "

        print("\nPalabra:", palabra_oculta)

        print("Letras utilizadas:", letras_usadas)

        # Comprobar si gano
        if all(letra in letras_usadas for letra in palabra):

            print("\n¡FELICIDADES! Adivinaste la palabra.")

            puntos = 100 - (errores.cantidad() * 15)

            break

        # Solicitar letra
        letra = input("\nIngresa una letra: ").upper()

        # Validar entrada
        if len(letra) != 1 or not letra.isalpha():

            print("Error: Ingresa solamente una letra.")

            continue

        # Comprobar si ya fue utilizada
        if letra in letras_usadas:

            print("Ya utilizaste esa letra.")

            continue

        # Guardar letra
        letras_usadas.append(letra)

        historial.agregar(letra)

        # Comprobar si existe en la palabra
        if letra in palabra:

            print("¡Correcto! La letra existe.")

        else:

            print("Incorrecto. Pierdes una oportunidad.")

            errores.apilar(letra)

    # Comprobar derrota
    if errores.cantidad() == 6:

        mostrar_ahorcado(6)

        print("\n¡PERDISTE!")

        print("La palabra correcta era:", palabra)

        puntos = 0

    # Mostrar resultados
    print("\n================================")
    print("       RESULTADO DE PARTIDA")
    print("================================")

    print("Jugador:", jugador)

    print("Puntuacion obtenida:", puntos)

    print("\nHistorial de letras:")

    historial.mostrar()

    print("\nLetras incorrectas:")

    errores.mostrar()

    return puntos


# =====================================================
# PARTE 5: PROGRAMA PRINCIPAL E INTEGRACION
# =====================================================

def main():

    jugadores = []

    print("\n================================")
    print("       BIENVENIDO AL AHORCADO")
    print("================================")

    continuar = "S"

    # Permitir varios jugadores
    while continuar == "S":

        nombre = input("\nIngresa tu nombre: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacio.")
            continue

        # Buscar jugador existente
        jugador = buscar_jugador(jugadores, nombre)

        if jugador is None:

            jugador = {
                "nombre": nombre,
                "puntos": 0
            }

            jugadores.append(jugador)

        # Crear cola de palabras
        palabras = Cola()

        palabras.encolar("PYTHON")

        palabras.encolar("COMPUTADORA")

        palabras.encolar("PROGRAMACION")

        # Tres rondas por jugador
        ronda = 1

        while ronda <= 3 and not palabras.esta_vacia():

            print("\n================================")
            print("           RONDA", ronda)
            print("================================")

            palabra = palabras.desencolar()

            puntos = jugar_palabra(palabra, nombre)

            jugador["puntos"] += puntos

            ronda += 1

        print("\nPuntos acumulados de", nombre, ":",
              jugador["puntos"])

        continuar = input(
            "\n¿Deseas agregar otro jugador? (S/N): "
        ).strip().upper()

    # Ordenar jugadores por puntuacion
    ordenar_jugadores(jugadores)

    # Mostrar clasificacion
    mostrar_clasificacion(jugadores)

    # Buscar un jugador
    print("\n================================")
    print("         BUSCAR JUGADOR")
    print("================================")

    busqueda = input("Escribe el nombre del jugador: ").strip()

    resultado = buscar_jugador(jugadores, busqueda)

    if resultado is not None:

        print("\n¡Jugador encontrado!")

        print("Nombre:", resultado["nombre"])

        print("Puntos:", resultado["puntos"])

    else:

        print("\nJugador no encontrado.")

    print("\n================================")
    print("       GRACIAS POR JUGAR")
    print("================================")


# Ejecutar el programa
if __name__ == "__main__":
    main()
