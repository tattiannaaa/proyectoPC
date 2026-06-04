ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"


def cargar_libros():
    libros = {}

    try:
        archivo = open(ARCHIVO_LIBROS, "r", encoding="utf-8")
    except FileNotFoundError:
        return libros

    for linea in archivo:
        datos = linea.strip().split(";")

        if len(datos) == 6:
            codigo = datos[0]
            libros[codigo] = {
                "codigo": datos[0],
                "titulo": datos[1],
                "autor": datos[2],
                "ano": int(datos[3]),
                "genero": datos[4],
                "estado": datos[5],
            }

    archivo.close()
    return libros


def guardar_libros(libros):
    archivo = open(ARCHIVO_LIBROS, "w", encoding="utf-8")

    for libro in libros.values():
        linea = (
            libro["codigo"] + ";"
            + libro["titulo"] + ";"
            + libro["autor"] + ";"
            + str(libro["ano"]) + ";"
            + libro["genero"] + ";"
            + libro["estado"] + "\n"
        )
        archivo.write(linea)

    archivo.close()


def cargar_prestamos():
    prestamos = []

    try:
        archivo = open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8")
    except FileNotFoundError:
        return prestamos

    for linea in archivo:
        datos = linea.strip().split(";")

        if len(datos) == 4:
            prestamo = {
                "codigo_libro": datos[0],
                "persona": datos[1],
                "fecha_prestamo": datos[2],
                "fecha_devolucion": datos[3],
            }
            prestamos.append(prestamo)

    archivo.close()
    return prestamos


def guardar_prestamos(prestamos):
    archivo = open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8")

    for prestamo in prestamos:
        linea = (
            prestamo["codigo_libro"] + ";"
            + prestamo["persona"] + ";"
            + prestamo["fecha_prestamo"] + ";"
            + prestamo["fecha_devolucion"] + "\n"
        )
        archivo.write(linea)

    archivo.close()
