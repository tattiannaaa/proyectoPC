# Modulo que necesitamos para leer los argumentos que se pasan por consola
import sys

import libros
import prestamos

def error_parametros():
    print("Error: faltan parámetros")

# sys.argv lista con todo lo que se escribio en consola
def main():
    # Chequea que haya al menos un elemento en sys.argv, si no lo hay, muestra un mensaje de error y termina la función
    if len(sys.argv) < 2:
        print("Error: debe indicar una operación")
        return

# Guardamos la variable en el segundo elemento de la lista
    operacion = sys.argv[1]

    match operacion:
        case "registrar_libro":
            if len(sys.argv) < 7:
                error_parametros()
                return
            libros.registrar_libro(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

        case "prestar_libro":
            if len(sys.argv) < 6:
                error_parametros()
                return
            prestamos.prestar_libro(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

        case "devolver_libro":
            if len(sys.argv) < 3:
                error_parametros()
                return
            prestamos.devolver_libro(sys.argv[2])

        case "listar_libros":
            estado = sys.argv[2] if len(sys.argv) > 2 else None
            libros.listar_libros(estado)

        case "listar_prestamos":
            prestamos.listar_prestamos()

        case _:
            print("Error: operación no reconocida")

if __name__ == "__main__":
    main()
