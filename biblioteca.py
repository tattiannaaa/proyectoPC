# Modulo que necesitamos para leer los argumentos que se pasan por consola
import sys

from libros import ESTADO_DISPONIBLE, ESTADO_PRESTADO, listar_libros, registrar_libro
from prestamos import devolver_libro, listar_prestamos, prestar_libro
    
# Estas estructuras guardan los datos mientras el programa esta abierto
libros = {}
prestamos = []

# Imprime en pantalla cada elemento de una lista
def _imprimir_lista(elementos):
    for elemento in elementos:
        print(elemento)

# Muestra las opciones del menu interactivo
def _mostrar_menu():
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
    
# Pide los datos del libro por teclado y lo registra
def _opcion_registrar_libro():
    codigo = input("Código: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    año = input("Año de publicación: ")
    genero = input("Género: ")
    print()
    print(registrar_libro(codigo, titulo, autor, año, genero))

# Pide los datos del préstamo por teclado y lo registra
def _opcion_prestar_libro():
    codigo = input("Código del libro: ")
    persona = input("Nombre de la persona: ")
    fecha_prestamo = input("Fecha del préstamo (AAAA-MM-DD): ")
    fecha_devolucion = input("Fecha esperada de devolución (AAAA-MM-DD): ")
    print()
    print(prestar_libro(codigo, persona, fecha_prestamo, fecha_devolucion))
    
# Pide el código del libro por teclado y registra la devolución
def _opcion_devolver_libro():
    codigo = input("Código del libro: ")
    print()
    print(devolver_libro(codigo))
    
# Ejecuta el programa con menu e ingreso de datos por teclado y se repite hasta que el usuario elige salir
def _ejecutar_modo_interactivo():
    opcion = ""
 
    while opcion != "0":
        _mostrar_menu()
        opcion = input("Ingrese una opción: ")
        print()
 
        match opcion:
            case "1":
                _opcion_registrar_libro()
            case "2":
                _opcion_prestar_libro()
            case "3":
                _opcion_devolver_libro()
            case "4":
                _imprimir_lista(listar_libros())
            case "5":
                _imprimir_lista(listar_libros(ESTADO_DISPONIBLE))
            case "6":
                _imprimir_lista(listar_libros(ESTADO_PRESTADO))
            case "7":
                _imprimir_lista(listar_prestamos())
            case "0":
                print("Programa finalizado.")
            case _:
                print("Error: Opción incorrecta.")

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
                print("Uso: python biblioteca.py prestar_libro CODIGO PERSONA FECHA_PRESTAMO FECHA_DEVOLUCION")
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
            print("Error: Operación incorrecta.")

def main():
    """
    Este es el punto de entrada del programa.
    Si no se pasan argumentos por consola, abre el menú interactivo.
    Si se pasan argumentos, ejecuta el comando correspondiente.
    """
    if len(sys.argv) == 1:
        _ejecutar_modo_interactivo()
    else:
        _ejecutar_comando(sys.argv[1:])

# Ejecuta main() solo si se corre este archivo directamente
if __name__ == "__main__":
    main()
