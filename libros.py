# Modulo para gestionar los libros de la biblioteca.
# Contiene funciones para registrar, listar y buscar libros.

from almacenamiento import cargar_datos, guardar_datos

# Constantes para los estados posibles de un libro
ESTADO_DISPONIBLE = "DISPONIBLE"
ESTADO_PRESTADO = "PRESTADO"

def registrar_libro(codigo, titulo, autor, año, genero):
    """
    Registra un nuevo libro en el sistema.
    Si ya existe un libro con ese código, retorna un error.
    """
    datos = cargar_datos()
    libros = datos["libros"]

    if codigo in libros:
        return f"Error: Ya existe un libro con el código {codigo}."

    if not año.isdigit():
        return "Error: El año de publicación debe ser un número."

    libros[codigo] = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "año": int(año),
        "genero": genero,
        "estado": ESTADO_DISPONIBLE,
    }

    guardar_datos(datos)
    return "Libro registrado con éxito."

def listar_libros(estado=None):
    """
    Lista los libros del sistema.
    Si se pasa un estado (DISPONIBLE o PRESTADO), filtra por ese estado.
    Si no se pasa estado, muestra todos.
    """
    datos = cargar_datos()
    libros = datos["libros"]
    resultado = []

    for libro in libros.values():
        if estado is None or libro["estado"] == estado:
            resultado.append(_formatear_libro(libro))

    if len(resultado) == 0:
        return ["No hay libros para mostrar."]

    return resultado

def buscar_libro(codigo):
    """
    Busca un libro por su código y lo retorna.
    Retorna el libro si lo encuentra, o None si no existe.
    """
    datos = cargar_datos()
    libros = datos["libros"]
    return libros.get(codigo)

def _formatear_libro(libro):
    # Arma el texto que se muestra por pantalla para un libro
    return (
        f"{libro['codigo']} | {libro['titulo']} | {libro['autor']} | "
        f"{libro['año']} | {libro['genero']} | {libro['estado']}"
    )
