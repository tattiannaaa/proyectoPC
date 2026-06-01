ESTADO_DISPONIBLE = "DISPONIBLE"
ESTADO_PRESTADO = "PRESTADO"


def registrar_libro(libros, codigo, titulo, autor, año, genero):
    # Agrega un libro nuevo al diccionario de libros.
    # Primero se controla que no exista otro libro con el mismo codigo.
    if codigo in libros:
        return f"Error: Ya existe un libro con el codigo {codigo}."

    # El año llega como texto, por eso se revisa antes de convertirlo a numero.
    if not año.isdigit():
        return "Error: El año de publicacion debe ser un numero."

    # Cada libro se guarda como un diccionario dentro del diccionario principal.
    libros[codigo] = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "año": int(año),
        "genero": genero,
        "estado": ESTADO_DISPONIBLE,
    }

    return "Libro registrado con exito."


def listar_libros(libros, estado=None):
    # Devuelve una lista de textos con los libros encontrados.
    resultado = []

    # Si estado es None, se listan todos los libros.
    # Si estado tiene un valor, se listan solo los que coinciden.
    for libro in libros.values():
        if estado is None or libro["estado"] == estado:
            resultado.append(formatear_libro(libro))

    if len(resultado) == 0:
        return ["No hay libros para mostrar."]

    return resultado


def formatear_libro(libro):
    # Arma el texto que se muestra por pantalla para un libro.
    return (
        f"{libro['codigo']} | {libro['titulo']} | {libro['autor']} | "
        f"{libro['año']} | {libro['genero']} | {libro['estado']}"
    )
