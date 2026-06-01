import sys

from funciones_libros import (
    ESTADO_DISPONIBLE,
    ESTADO_PRESTADO,
    listar_libros,
    registrar_libro,
)
from funciones_prestamos import (
    devolver_libro,
    listar_prestamos,
    prestar_libro,
)

# Estas estructuras guardan los datos mientras el programa esta abierto.
libros = {}
prestamos = []

def mostrar_menu():
    # Muestra las opciones del menu interactivo.
    print()
    print("SISTEMA DE BIBLIOTECA")
    print("1 - Registrar libro")
    print("2 - Prestar libro")
    print("3 - Devolver libro")
    print("4 - Listar todos los libros")
    print("5 - Listar libros disponibles")
    print("6 - Listar libros prestados")
    print("7 - Listar prestamos activos")
    print("0 - Salir")
    print()


def ejecutar_modo_interactivo():
    # Ejecuta el programa con menu e ingreso de datos por teclado.
    opcion = ""

    # El menu se repite hasta que el usuario elige salir.
    while opcion != "0":
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print()
            print("Ingrese los siguientes datos")
            codigo = input("Codigo: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            año = input("Año de publicacion: ")
            genero = input("Genero: ")
            print()
            print(registrar_libro(libros, codigo, titulo, autor, año, genero))

        elif opcion == "2":
            print()
            print("Ingrese los siguientes datos")
            codigo = input("Codigo del libro: ")
            persona = input("Nombre de la persona: ")
            fecha_prestamo = input("Fecha del prestamo (AAAA-MM-DD): ")
            fecha_devolucion = input("Fecha esperada de devolucion (AAAA-MM-DD): ")
            print()
            print(prestar_libro(libros, prestamos, codigo, persona, fecha_prestamo, fecha_devolucion))

        elif opcion == "3":
            print()
            print("Ingrese el codigo de su libro a devolver")
            codigo = input("Codigo del libro: ")
            print()
            print(devolver_libro(libros, prestamos, codigo))

        elif opcion == "4":
            print() 
            imprimir_lista(listar_libros(libros))

        elif opcion == "5":
            print()
            imprimir_lista(listar_libros(libros, ESTADO_DISPONIBLE))

        elif opcion == "6":
            print()
            imprimir_lista(listar_libros(libros, ESTADO_PRESTADO))

        elif opcion == "7":
            print()
            imprimir_lista(listar_prestamos(prestamos))

        elif opcion == "0":
            print()
            print("Programa finalizado.")

        else:
            print()
            print("Error: Opcion incorrecta.")


def imprimir_lista(elementos):
    # Imprime en pantalla cada elemento de una lista.
    for elemento in elementos:
        print(elemento)


def ejecutar_comando(argumentos):
    # Ejecuta una operacion recibida por consola.
    operacion = argumentos[0]

    if operacion == "registrar_libro":
        if len(argumentos) != 6:
            print("Uso: python biblioteca.py registrar_libro CODIGO TITULO AUTOR AÑO GENERO")
            return

        print(registrar_libro(libros, argumentos[1], argumentos[2], argumentos[3], argumentos[4], argumentos[5]))

    elif operacion == "prestar_libro":
        if len(argumentos) != 5:
            print("Uso: python biblioteca.py prestar_libro CODIGO PERSONA FECHA_PRESTAMO FECHA_DEVOLUCION")
            return

        print(prestar_libro(libros, prestamos, argumentos[1], argumentos[2], argumentos[3], argumentos[4]))

    elif operacion == "devolver_libro":
        if len(argumentos) != 2:
            print("Uso: python biblioteca.py devolver_libro CODIGO")
            return

        print(devolver_libro(libros, prestamos, argumentos[1]))

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
    # Decide si se usa menu interactivo o comando por consola.
    if len(sys.argv) == 1:
        ejecutar_modo_interactivo()
    else:
        ejecutar_comando(sys.argv[1:])


if __name__ == "__main__":
    main()
