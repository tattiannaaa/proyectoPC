from libros import (
    ESTADO_DISPONIBLE,
    ESTADO_PRESTADO,
    listar_libros,
    registrar_libro,
)
from prestamos import devolver_libro, listar_prestamos, prestar_libro


def test_registrar_libro():
    libros = {}

    mensaje = registrar_libro(
        libros,
        "L001",
        "El principito",
        "Antoine de Saint-Exupery",
        "1943",
        "Novela",
    )

    assert mensaje == "Libro registrado con exito."
    assert "L001" in libros
    assert libros["L001"]["estado"] == ESTADO_DISPONIBLE


def test_no_permite_codigo_repetido():
    libros = {}

    registrar_libro(libros, "L001", "Libro 1", "Autor 1", "2000", "Drama")
    mensaje = registrar_libro(libros, "L001", "Libro 2", "Autor 2", "2020", "Novela")

    assert mensaje == "Error: Ya existe un libro con el codigo L001."
    assert len(libros) == 1


def test_prestar_libro():
    libros = {}
    prestamos = []

    registrar_libro(libros, "L001", "El principito", "Autor", "1943", "Novela")
    mensaje = prestar_libro(libros, prestamos, "L001", "Juan Perez", "2026-06-01", "2026-06-15")

    assert mensaje == "Libro prestado con exito."
    assert libros["L001"]["estado"] == ESTADO_PRESTADO
    assert len(prestamos) == 1


def test_no_prestar_libro_inexistente():
    libros = {}
    prestamos = []

    mensaje = prestar_libro(libros, prestamos, "L999", "Ana", "2026-06-01", "2026-06-10")

    assert mensaje == "Error: No existe un libro con el codigo L999."


def test_no_prestar_libro_ya_prestado():
    libros = {}
    prestamos = []

    registrar_libro(libros, "L001", "El principito", "Autor", "1943", "Novela")
    prestar_libro(libros, prestamos, "L001", "Juan Perez", "2026-06-01", "2026-06-15")
    mensaje = prestar_libro(libros, prestamos, "L001", "Ana Lopez", "2026-06-20", "2026-06-30")

    assert mensaje == "Error: El libro L001 no esta disponible."


def test_no_prestar_con_fecha_incorrecta():
    libros = {}
    prestamos = []

    registrar_libro(libros, "L001", "El principito", "Autor", "1943", "Novela")
    mensaje = prestar_libro(libros, prestamos, "L001", "Juan Perez", "2026-06-15", "2026-06-01")

    assert mensaje == "Error: La fecha esperada de devolucion no puede ser anterior a la fecha del prestamo."


def test_devolver_libro():
    libros = {}
    prestamos = []

    registrar_libro(libros, "L001", "El principito", "Autor", "1943", "Novela")
    prestar_libro(libros, prestamos, "L001", "Juan Perez", "2026-06-01", "2026-06-15")
    mensaje = devolver_libro(libros, prestamos, "L001")

    assert mensaje == "Libro devuelto con exito."
    assert libros["L001"]["estado"] == ESTADO_DISPONIBLE
    assert len(prestamos) == 0


def test_listar_libros_y_prestamos():
    libros = {}
    prestamos = []

    registrar_libro(libros, "L001", "Libro 1", "Autor", "2000", "Drama")
    prestar_libro(libros, prestamos, "L001", "Juan", "2026-06-01", "2026-06-15")

    assert len(listar_libros(libros)) == 1
    assert len(listar_libros(libros, ESTADO_PRESTADO)) == 1
    assert len(listar_prestamos(prestamos)) == 1


def ejecutar_tests():
    test_registrar_libro()
    test_no_permite_codigo_repetido()
    test_prestar_libro()
    test_no_prestar_libro_inexistente()
    test_no_prestar_libro_ya_prestado()
    test_no_prestar_con_fecha_incorrecta()
    test_devolver_libro()
    test_listar_libros_y_prestamos()
    print("Todos los tests pasaron.")


if __name__ == "__main__":
    ejecutar_tests()
