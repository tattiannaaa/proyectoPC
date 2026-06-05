# Modulo para gestionar los prestamos de la biblioteca.
# Contiene funciones para prestar, devolver y listar prestamos.

from datetime import datetime

from almacenamiento import cargar_datos, guardar_datos
from libros import ESTADO_DISPONIBLE, ESTADO_PRESTADO

# Formato de fecha que usa el sistema
FORMATO_FECHA = "%Y-%m-%d"

def _fecha_valida(fecha):
    """
    Retorna True si la fecha tiene el formato AAAA-MM-DD, False si no.
    La barra baja al inicio indica que es una función interna del módulo.
    """
    try:
        datetime.strptime(fecha, FORMATO_FECHA)
        return True
    except ValueError:
        return False

def prestar_libro(codigo, persona, fecha_prestamo, fecha_devolucion):
    """
    Registra el préstamo de un libro a una persona.
    Valida que el libro exista, esté disponible y que las fechas sean correctas.
    """
    datos = cargar_datos()

    # No se puede prestar un libro que no está registrado
    if codigo not in datos["libros"]:
        return f"Error: No existe un libro con el código {codigo}."

    # Solo se puede prestar si el libro está disponible
    if datos["libros"][codigo]["estado"] != ESTADO_DISPONIBLE:
        return f"Error: El libro {codigo} no está disponible."

    # Las dos fechas deben tener el formato pedido por la consigna
    if not _fecha_valida(fecha_prestamo) or not _fecha_valida(fecha_devolucion):
        return "Error: Las fechas deben tener formato AAAA-MM-DD."

    fecha_inicio = datetime.strptime(fecha_prestamo, FORMATO_FECHA)
    fecha_fin = datetime.strptime(fecha_devolucion, FORMATO_FECHA)

    # La devolución esperada no puede ser antes del préstamo
    if fecha_fin < fecha_inicio:
        return "Error: La fecha esperada de devolución no puede ser anterior a la fecha del préstamo."

    prestamo = {
        "codigo_libro": codigo,
        "persona": persona,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
    }

    datos["prestamos"].append(prestamo)
    datos["libros"][codigo]["estado"] = ESTADO_PRESTADO

    guardar_datos(datos)
    return "Libro prestado con éxito."

def devolver_libro(codigo):
    """
    Registra la devolución de un libro prestado.
    Valida que el libro exista y esté en estado PRESTADO.
    """
    datos = cargar_datos()

    # No se puede devolver un libro que no existe
    if codigo not in datos["libros"]:
        return f"Error: No existe un libro con el código {codigo}."

    # Solo se puede devolver si el libro figura como prestado.
    if datos["libros"][codigo]["estado"] != ESTADO_PRESTADO:
        return f"Error: El libro {codigo} no está prestado."

    datos["libros"][codigo]["estado"] = ESTADO_DISPONIBLE

    # Se busca el préstamo activo del libro y se elimina de la lista
    for prestamo in datos["prestamos"]:
        if prestamo["codigo_libro"] == codigo:
            datos["prestamos"].remove(prestamo)
            break

    guardar_datos(datos)
    return "Libro devuelto con éxito."

def listar_prestamos():
    # Devuelve una lista de textos con los préstamos activos
    datos = cargar_datos()
    resultado = []

    for prestamo in datos["prestamos"]:
        resultado.append(_formatear_prestamo(prestamo))

    if len(resultado) == 0:
        return ["No hay préstamos activos."]

    return resultado

def _formatear_prestamo(prestamo):
    """
    Arma el texto que se muestra por pantalla para un préstamo.
    La barra baja al inicio indica que es una función interna del módulo.
    """
    return (
        f"Libro: {prestamo['codigo_libro']} | Persona: {prestamo['persona']} | "
        f"Préstamo: {prestamo['fecha_prestamo']} | "
        f"Devolución esperada: {prestamo['fecha_devolucion']}"
    )
