import unittest

from funciones_libros import (
    ESTADO_DISPONIBLE,
    ESTADO_PRESTADO,
    listar_libros,
    registrar_libro,
)
from funciones_prestamos import devolver_libro, listar_prestamos, prestar_libro


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        # Cada test empieza con datos vacios para no depender de otro test.
        self.libros = {}
        self.prestamos = []

    def test_registrar_libro(self):
        # Prueba que un libro nuevo se agregue con estado DISPONIBLE.
        mensaje = registrar_libro(
            self.libros,
            "L001",
            "El principito",
            "Antoine de Saint-Exupery",
            "1943",
            "Novela",
        )

        self.assertEqual(mensaje, "Libro registrado con exito.")
        self.assertIn("L001", self.libros)
        self.assertEqual(self.libros["L001"]["estado"], ESTADO_DISPONIBLE)

    def test_no_permite_codigo_repetido(self):
        # Prueba que no se puedan registrar dos libros con el mismo codigo.
        registrar_libro(self.libros, "L001", "Libro 1", "Autor 1", "2000", "Drama")
        mensaje = registrar_libro(self.libros, "L001", "Libro 2", "Autor 2", "2020", "Novela")

        self.assertEqual(mensaje, "Error: Ya existe un libro con el codigo L001.")
        self.assertEqual(len(self.libros), 1)

    def test_prestar_libro(self):
        # Prueba que al prestar un libro cambie a estado PRESTADO.
        registrar_libro(self.libros, "L001", "El principito", "Autor", "1943", "Novela")
        mensaje = prestar_libro(self.libros, self.prestamos, "L001", "Juan Perez", "2026-06-01", "2026-06-15")

        self.assertEqual(mensaje, "Libro prestado con exito.")
        self.assertEqual(self.libros["L001"]["estado"], ESTADO_PRESTADO)
        self.assertEqual(len(self.prestamos), 1)

    def test_no_prestar_libro_inexistente(self):
        # Prueba el error al intentar prestar un codigo que no existe.
        mensaje = prestar_libro(self.libros, self.prestamos, "L999", "Ana", "2026-06-01", "2026-06-10")

        self.assertEqual(mensaje, "Error: No existe un libro con el codigo L999.")

    def test_no_prestar_libro_ya_prestado(self):
        # Prueba que un libro prestado no se pueda prestar otra vez.
        registrar_libro(self.libros, "L001", "El principito", "Autor", "1943", "Novela")
        prestar_libro(self.libros, self.prestamos, "L001", "Juan Perez", "2026-06-01", "2026-06-15")
        mensaje = prestar_libro(self.libros, self.prestamos, "L001", "Ana Lopez", "2026-06-20", "2026-06-30")

        self.assertEqual(mensaje, "Error: El libro L001 no esta disponible.")

    def test_no_prestar_con_fecha_incorrecta(self):
        # Prueba que la devolucion no pueda ser antes del prestamo.
        registrar_libro(self.libros, "L001", "El principito", "Autor", "1943", "Novela")
        mensaje = prestar_libro(self.libros, self.prestamos, "L001", "Juan Perez", "2026-06-15", "2026-06-01")

        self.assertEqual(
            mensaje,
            "Error: La fecha esperada de devolucion no puede ser anterior a la fecha del prestamo.",
        )

    def test_devolver_libro(self):
        # Prueba que devolver un libro lo deje disponible otra vez.
        registrar_libro(self.libros, "L001", "El principito", "Autor", "1943", "Novela")
        prestar_libro(self.libros, self.prestamos, "L001", "Juan Perez", "2026-06-01", "2026-06-15")
        mensaje = devolver_libro(self.libros, self.prestamos, "L001")

        self.assertEqual(mensaje, "Libro devuelto con exito.")
        self.assertEqual(self.libros["L001"]["estado"], ESTADO_DISPONIBLE)
        self.assertEqual(len(self.prestamos), 0)

    def test_listar_libros_y_prestamos(self):
        # Prueba que los listados devuelvan los elementos esperados.
        registrar_libro(self.libros, "L001", "Libro 1", "Autor", "2000", "Drama")
        prestar_libro(self.libros, self.prestamos, "L001", "Juan", "2026-06-01", "2026-06-15")

        self.assertEqual(len(listar_libros(self.libros)), 1)
        self.assertEqual(len(listar_libros(self.libros, ESTADO_PRESTADO)), 1)
        self.assertEqual(len(listar_prestamos(self.prestamos)), 1)


if __name__ == "__main__":
    unittest.main()
