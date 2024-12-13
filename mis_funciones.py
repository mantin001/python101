import time
import sqlite3

# Paso 1: Definir clases para modelar las tablas de la base de datos
class Disco:
    def __init__(self, ID, NAME, DURATION, AUTHOR):
        self.ID = ID
        self.NAME = NAME  # Cambié 'Name' a 'NAME'
        self.DURATION = DURATION  # Cambié 'Duration' a 'DURATION'
        self.AUTHOR = AUTHOR  # Cambié 'Author' a 'AUTHOR'

###############1. Leer la carátula################
def caratula(demos):
    # Iterar sobre la lista de discos y mostrar la información
    for demo in demos:
        print(f"ID: {demo.ID}, Name: {demo.NAME}, Duration: {demo.DURATION}, Author: {demo.AUTHOR}")

###############2. Escuchar todo el disco################
def escuchar(demos):
    print("Estás escuchando el disco... 🎵")
    for demo in demos:
        print(f"\nReproduciendo: {demo.NAME} ({demo.DURATION})")
        print("▶️ Reproduciendo...")  # Icono de "play"

        minutes, seconds = map(int, demo.DURATION.split(":"))
        duration_in_seconds = minutes * 1 + seconds

        time.sleep(duration_in_seconds)

        print("⏸️ Pausa...")  # Icono de "pause"
        time.sleep(1)  # Simulamos una pausa de 1 segundo entre canciones

    print("\n¡Disco terminado! 🎶")

###############3. Añadir una canción################
def añadir_cancion(demos, connection):
    cursor = connection.cursor()
    name = str(input("Escriba el nombre de la canción: "))
    duration = str(input("Escriba la duración de la canción, formato [mm:ss]: "))
    author = str(input("Escriba el nombre del autor: "))

    # Validar formato de duración
    if not validate_duration(duration):
        print("El formato de duración debe ser mm:ss.")
        return

    # Añadir la canción a la base de datos
    cursor.execute("INSERT INTO Disco (NAME, DURATION, AUTHOR) VALUES (?, ?, ?)", (name, duration, author))
    connection.commit()

    # Recuperar el ID recién generado
    nuevo_id = cursor.lastrowid
    cancion = Disco(nuevo_id, name, duration, author)
    demos.append(cancion)

    print(f"\nLa canción '{name}' ha sido añadida al disco con ID {nuevo_id}.")
    print("\nCarátula actualizada:")
    caratula(demos)

###############4. Eliminar una canción################
def eliminar_cancion(demos, connection):
    cursor = connection.cursor()
    print("¿Qué canción quieres eliminar?")
    caratula(demos)  # Mostrar la lista actual de canciones

    try:
        id_eliminar = int(input("Escribe el ID de la canción a eliminar: "))
    except ValueError:
        print("Por favor, introduce un ID válido.")
        return

    # Eliminar de la base de datos
    cursor.execute("DELETE FROM Disco WHERE ID = ?", (id_eliminar,))
    connection.commit()

    # Verificar si la canción fue eliminada
    if cursor.rowcount == 0:
        print(f"No se encontró ninguna canción con ID {id_eliminar}.")
        return

    # Eliminar de la lista local
    demos[:] = [demo for demo in demos if demo.ID != id_eliminar]

    print(f"\nLa canción con ID {id_eliminar} ha sido eliminada.")
    print("\nCarátula actualizada:")
    caratula(demos)

###############5. Consultar el autor de una canción################
def consultar_autor(demos):
    print("Consulta el autor de una canción")
    caratula(demos)  # Mostrar la lista de canciones para facilitar la selección

    try:
        id_buscar = int(input("Escribe el ID de la canción para consultar su autor: "))
    except ValueError:
        print("Por favor, introduce un ID válido.")
        return

    # Buscar la canción por su ID
    for demo in demos:
        if demo.ID == id_buscar:
            print(f"El autor de la canción '{demo.NAME}' es {demo.AUTHOR}.")
            return

    print(f"No se encontró ninguna canción con ID {id_buscar}.")

###############6. Reproducir una canción################
def reproducir_cancion(demos):
    print("¿Qué canción quieres escuchar?")
    caratula(demos)  # Mostrar la lista de canciones

    try:
        id_reproducir = int(input("Escribe el ID de la canción que deseas reproducir: "))
    except ValueError:
        print("Por favor, introduce un ID válido.")
        return

    # Buscar la canción por su ID
    for demo in demos:
        if demo.ID == id_reproducir:
            print(f"Reproduciendo: '{demo.NAME}'")
            print("▶️ Reproduciendo...")  # Icono de "play"

            minutes, seconds = map(int, demo.DURATION.split(":"))
            duration_in_seconds = minutes * 1 + seconds

            time.sleep(duration_in_seconds)

            print("⏸️ Pausa...")  # Icono de "pause"
            return

    print(f"No se encontró ninguna canción con ID {id_reproducir}.")

############### Función auxiliar: Validar formato de duración ################
def validate_duration(duration):
    import re
    return re.match(r"^\d{2}:\d{2}$", duration) is not None
