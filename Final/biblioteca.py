import sys

from almacenamiento import (
    cargar_libros,
    cargar_prestamos,
    guardar_libros,
    guardar_prestamos,
)
from libros import (
    ESTADO_DISPONIBLE,
    ESTADO_PRESTADO,
    listar_libros,
    registrar_libro,
)
from prestamos import (
    devolver_libro,
    listar_prestamos,
    prestar_libro,
)


def imprimir_lista(elementos):
    # Imprime en pantalla cada elemento de una lista.
    for elemento in elementos:
        print(elemento)


def guardar_datos(libros, prestamos):
    guardar_libros(libros)
    guardar_prestamos(prestamos)


def mostrar_ayuda():
    print()
    print("Operaciones disponibles:")
    print('python biblioteca.py registrar_libro "CODIGO" "TITULO" "AUTOR" "AÑO" "GENERO"')
    print('python biblioteca.py prestar_libro "CODIGO" "PERSONA" "FECHA PRESTAMO" "FECHA DEVOLUCION"')
    print('python biblioteca.py devolver_libro "CODIGO"')
    print("python biblioteca.py listar_libros")
    print("python biblioteca.py listar_libros DISPONIBLE")
    print("python biblioteca.py listar_libros PRESTADO")
    print("python biblioteca.py listar_prestamos")
    print()


def ejecutar_comando(argumentos):
    # Ejecuta una operacion recibida por consola.
    libros = cargar_libros()
    prestamos = cargar_prestamos()
    operacion = argumentos[0]

    if operacion == "ayuda":
        mostrar_ayuda()

    elif operacion == "registrar_libro":
        if len(argumentos) != 6:
            print("Uso: python biblioteca.py registrar_libro CODIGO TITULO AUTOR ANO GENERO")
            return

        mensaje = registrar_libro(libros, argumentos[1], argumentos[2], argumentos[3], argumentos[4], argumentos[5])
        print(mensaje)

        if mensaje == "Libro registrado con exito.":
            guardar_datos(libros, prestamos)

    elif operacion == "prestar_libro":
        if len(argumentos) != 5:
            print("Uso: python biblioteca.py prestar_libro CODIGO PERSONA FECHA_PRESTAMO FECHA_DEVOLUCION")
            return

        mensaje = prestar_libro(libros, prestamos, argumentos[1], argumentos[2], argumentos[3], argumentos[4])
        print(mensaje)

        if mensaje == "Libro prestado con exito.":
            guardar_datos(libros, prestamos)

    elif operacion == "devolver_libro":
        if len(argumentos) != 2:
            print("Uso: python biblioteca.py devolver_libro CODIGO")
            return

        mensaje = devolver_libro(libros, prestamos, argumentos[1])
        print(mensaje)

        if mensaje == "Libro devuelto con exito.":
            guardar_datos(libros, prestamos)

    elif operacion == "listar_libros":
        if len(argumentos) == 1:
            imprimir_lista(listar_libros(libros))
        elif len(argumentos) == 2 and argumentos[1] in [ESTADO_DISPONIBLE, ESTADO_PRESTADO]:
            imprimir_lista(listar_libros(libros, argumentos[1]))
        else:
            print("Uso: python biblioteca.py listar_libros [DISPONIBLE|PRESTADO]")

    elif operacion == "listar_prestamos":
        if len(argumentos) != 1:
            print("Uso: python biblioteca.py listar_prestamos")
            return

        imprimir_lista(listar_prestamos(prestamos))

    else:
        print("Error: Operacion incorrecta.")


def main():
    if len(sys.argv) == 1:
        mostrar_ayuda()
    else:
        ejecutar_comando(sys.argv[1:])


if __name__ == "__main__":
    main()
