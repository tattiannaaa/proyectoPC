# Modulo que necesitamos para leer los argumentos que se pasan por consola
import sys

from libros import ESTADO_DISPONIBLE, ESTADO_PRESTADO, listar_libros, registrar_libro
from prestamos import devolver_libro, listar_prestamos, prestar_libro


# Imprime en pantalla cada elemento de una lista
def _imprimir_lista(elementos):
    for elemento in elementos:
        print(elemento)


# Muestra una guia de comandos para usar el programa desde la terminal
def _mostrar_ayuda():
    print()
    print("SISTEMA DE BIBLIOTECA")
    print()
    print("Ingrese uno de estos comandos:")
    print()
    print('python biblioteca.py registrar_libro "CODIGO" "TITULO" "AUTOR" "AÑO" "GENERO"')
    print()
    print('python biblioteca.py prestar_libro "CODIGO" "NOMBRE" "FECHA PRESTAMO" "FECHA DEVOLUCION"')
    print()
    print('python biblioteca.py devolver_libro "CODIGO"')
    print()
    print("python biblioteca.py listar_libros")
    print()
    print("python biblioteca.py listar_libros DISPONIBLE")
    print()
    print("python biblioteca.py listar_libros PRESTADO")
    print()
    print("python biblioteca.py listar_prestamos")
    print()


# Ejecuta una operacion recibida por consola
def _ejecutar_comando(argumentos):
    operacion = argumentos[0]

    match operacion:
        case "registrar_libro":
            if len(argumentos) != 6:
                print("Uso: python biblioteca.py registrar_libro CODIGO TITULO AUTOR AÑO GENERO")
                return
            print(registrar_libro(argumentos[1], argumentos[2], argumentos[3], argumentos[4], argumentos[5]))

        case "prestar_libro":
            if len(argumentos) != 5:
                print("Uso: python biblioteca.py prestar_libro CODIGO NOMBRE FECHA_PRESTAMO FECHA_DEVOLUCION")
                return
            print(prestar_libro(argumentos[1], argumentos[2], argumentos[3], argumentos[4]))

        case "devolver_libro":
            if len(argumentos) != 2:
                print("Uso: python biblioteca.py devolver_libro CODIGO")
                return
            print(devolver_libro(argumentos[1]))

        case "listar_libros":
            if len(argumentos) == 1:
                _imprimir_lista(listar_libros())
            elif len(argumentos) == 2 and argumentos[1] in [ESTADO_DISPONIBLE, ESTADO_PRESTADO]:
                _imprimir_lista(listar_libros(argumentos[1]))
            else:
                print("Uso: python biblioteca.py listar_libros [DISPONIBLE|PRESTADO]")

        case "listar_prestamos":
            if len(argumentos) != 1:
                print("Uso: python biblioteca.py listar_prestamos")
                return
            _imprimir_lista(listar_prestamos())

        case _:
            print("Error: Operacion incorrecta.")
            _mostrar_ayuda()


def main():
    # Este es el punto de entrada del programa.
    # Si no se pasan argumentos por consola, muestra la ayuda.
    # Si se pasan argumentos, ejecuta el comando correspondiente.
  
    if len(sys.argv) == 1:
        _mostrar_ayuda()
    else:
        _ejecutar_comando(sys.argv[1:])


# Ejecuta main() solo si se corre este archivo directamente
if __name__ == "__main__":
    main()
