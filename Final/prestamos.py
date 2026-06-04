from datetime import datetime

from libros import ESTADO_DISPONIBLE, ESTADO_PRESTADO


def fecha_valida(fecha):
    # Devuelve True si la fecha tiene formato AAAA-MM-DD.
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def prestar_libro(libros, prestamos, codigo, persona, fecha_prestamo, fecha_devolucion):
    # Registra el prestamo de un libro a una persona.
    # No se puede prestar un libro que no esta registrado.
    if codigo not in libros:
        return f"Error: No existe un libro con el codigo {codigo}."

    # Solo se puede prestar si el libro esta disponible.
    if libros[codigo]["estado"] != ESTADO_DISPONIBLE:
        return f"Error: El libro {codigo} no esta disponible."

    # Las dos fechas deben tener el formato pedido por la consigna.
    if not fecha_valida(fecha_prestamo) or not fecha_valida(fecha_devolucion):
        return "Error: Las fechas deben tener formato AAAA-MM-DD."

    fecha_inicio = datetime.strptime(fecha_prestamo, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_devolucion, "%Y-%m-%d")

    # La devolucion esperada no puede ser antes del prestamo.
    if fecha_fin < fecha_inicio:
        return "Error: La fecha esperada de devolucion no puede ser anterior a la fecha del prestamo."

    prestamo = {
        "codigo_libro": codigo,
        "persona": persona,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
    }

    prestamos.append(prestamo)
    libros[codigo]["estado"] = ESTADO_PRESTADO

    return "Libro prestado con exito."


def devolver_libro(libros, prestamos, codigo):
    # Registra la devolucion de un libro prestado.
    # No se puede devolver un libro que no existe.
    if codigo not in libros:
        return f"Error: No existe un libro con el codigo {codigo}."

    # Solo se puede devolver si el libro figura como prestado.
    if libros[codigo]["estado"] != ESTADO_PRESTADO:
        return f"Error: El libro {codigo} no esta prestado."

    libros[codigo]["estado"] = ESTADO_DISPONIBLE

    # Se busca el prestamo activo del libro y se elimina de la lista.
    for prestamo in prestamos:
        if prestamo["codigo_libro"] == codigo:
            prestamos.remove(prestamo)

    return "Libro devuelto con exito."


def listar_prestamos(prestamos):
    # Devuelve una lista de textos con los prestamos activos.
    resultado = []

    for prestamo in prestamos:
        resultado.append(formatear_prestamo(prestamo))

    if len(resultado) == 0:
        return ["No hay prestamos activos."]

    return resultado


def formatear_prestamo(prestamo):
    # Arma el texto que se muestra por pantalla para un prestamo.
    return (
        f"Libro: {prestamo['codigo_libro']} | Persona: {prestamo['persona']} | "
        f"Prestamo: {prestamo['fecha_prestamo']} | "
        f"Devolucion esperada: {prestamo['fecha_devolucion']}"
    )
