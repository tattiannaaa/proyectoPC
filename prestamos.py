import libros

# Cada prestamo es un diccionario con sus atributos
prestamos = []

def prestar_libro(codigo, persona, fecha_prestamo, fecha_devolucion):
    """
    Registra el prestamo de un libro a una persona.
    Valida que el libro exista, este disponible y que las fechas sean correctas.
    """
    # Buscamos el libro por su codigo
    libro = libros.buscar_libro(codigo)

    # Verificamos que el libro exista
    if libro == None:
        print("Error: No existe un libro con el código", codigo)
        return

    # Vemos si el libro está disponible
    if libro["estado"] != "DISPONIBLE":
        print("Error: El libro", codigo, "no está disponible.")
        return

    # Chequea que la fecha de devolucion no sea anterior a la de prestamo
    if fecha_devolucion < fecha_prestamo:
        print("Error: La fecha de devolución no puede ser anterior a la fecha de préstamo.")
        return

    # Diccionario con los datos del prestamo
    nuevo_prestamo = {
        "codigo_libro": codigo,
        "persona": persona,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion
    }

    # Lo agregamos a la lista de prestamos
    prestamos.append(nuevo_prestamo)

    # Cambiamos el estado del libro a PRESTADO
    libro["estado"] = "PRESTADO"

    print("Libro prestado con éxito.")


def devolver_libro(codigo):
    """
    Registra la devolucion de un libro prestado.
    Valida que el libro exista y este en estado PRESTADO.
    """
    # Buscamos el libro por su codigo
    libro = libros.buscar_libro(codigo)

    # Verificamos que el libro exista
    if libro == None:
        print("Error: No existe un libro con el código", codigo)
        return

    # Verificamos que el libro este prestado
    if libro["estado"] != "PRESTADO":
        print("Error: El libro", codigo, "no está prestado.")
        return

    # Cambiamos el estado del libro a DISPONIBLE
    libro["estado"] = "DISPONIBLE"
    
    # Eliminamos el prestamo de la lista
    for prestamo in prestamos:
        if prestamo["codigo_libro"] == codigo:
            prestamos.remove(prestamo)

    print("Libro devuelto con éxito.")


def listar_prestamos():
    """
    Lista todos los prestamos activos del sistema.
    """
    # Verificamos que haya prestamos registrados
    if len(prestamos) == 0:
        print("No hay préstamos activos.")
        return

    for prestamo in prestamos:
        print("Libro:", prestamo["codigo_libro"],
              "| Persona:", prestamo["persona"],
              "| Fecha préstamo:", prestamo["fecha_prestamo"],
              "| Fecha devolución:", prestamo["fecha_devolucion"])
