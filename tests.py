from almacenamiento import guardar_datos
from libros import ESTADO_DISPONIBLE, ESTADO_PRESTADO, buscar_libro, listar_libros, registrar_libro
from prestamos import devolver_libro, listar_prestamos, prestar_libro

def limpiar():
    # Cada test empieza con datos vacíos para no depender de otro test.
    guardar_datos({"libros": {}, "prestamos": []})

def test_registrar_libro():
    # Prueba que un libro nuevo se agregue con estado DISPONIBLE.
    limpiar()
    mensaje = registrar_libro("L001", "El principito", "Antoine de Saint-Exupéry", "1943", "Novela")

    assert mensaje == "Libro registrado con éxito."
    assert "L001" in buscar_libro("L001").values() or buscar_libro("L001") is not None
    assert buscar_libro("L001")["estado"] == ESTADO_DISPONIBLE

def test_no_permite_codigo_repetido():
    # Prueba que no se puedan registrar dos libros con el mismo código.
    limpiar()
    registrar_libro("L001", "Libro 1", "Autor 1", "2000", "Drama")
    mensaje = registrar_libro("L001", "Libro 2", "Autor 2", "2020", "Novela")

    assert mensaje == "Error: Ya existe un libro con el código L001."
    assert len(listar_libros()) == 1

def test_año_invalido():
    # Prueba que no se acepte un año que no sea número.
    limpiar()
    mensaje = registrar_libro("L001", "El principito", "Antoine", "mil", "Novela")

    assert mensaje == "Error: El año de publicación debe ser un número."
    assert listar_libros() == ["No hay libros para mostrar."]

def test_prestar_libro():
    # Prueba que al prestar un libro cambie a estado PRESTADO.
    limpiar()
    registrar_libro("L001", "El principito", "Antoine", "1943", "Novela")
    mensaje = prestar_libro("L001", "Juan Pérez", "2026-06-01", "2026-06-15")

    assert mensaje == "Libro prestado con éxito."
    assert buscar_libro("L001")["estado"] == ESTADO_PRESTADO
    assert len(listar_prestamos()) == 1

def test_no_prestar_libro_inexistente():
    # Prueba el error al intentar prestar un código que no existe.
    limpiar()
    mensaje = prestar_libro("L999", "Ana", "2026-06-01", "2026-06-10")

    assert mensaje == "Error: No existe un libro con el código L999."

def test_no_prestar_libro_ya_prestado():
    # Prueba que un libro prestado no se pueda prestar otra vez.
    limpiar()
    registrar_libro("L001", "El principito", "Antoine", "1943", "Novela")
    prestar_libro("L001", "Juan Pérez", "2026-06-01", "2026-06-15")
    mensaje = prestar_libro("L001", "Ana López", "2026-06-20", "2026-06-30")

    assert mensaje == "Error: El libro L001 no está disponible."

def test_no_prestar_con_fecha_incorrecta():
    # Prueba que la devolución no pueda ser antes del préstamo.
    limpiar()
    registrar_libro("L001", "El principito", "Antoine", "1943", "Novela")
    mensaje = prestar_libro("L001", "Juan Pérez", "2026-06-15", "2026-06-01")

    assert mensaje == "Error: La fecha esperada de devolución no puede ser anterior a la fecha del préstamo."

def test_no_prestar_con_formato_fecha_invalido():
    # Prueba que se rechacen fechas con formato incorrecto.
    limpiar()
    registrar_libro("L001", "El principito", "Antoine", "1943", "Novela")
    mensaje = prestar_libro("L001", "Juan Pérez", "01-06-2026", "15-06-2026")

    assert mensaje == "Error: Las fechas deben tener formato AAAA-MM-DD."

def test_devolver_libro():
    # Prueba que devolver un libro lo deje disponible y elimine el préstamo.
    limpiar()
    registrar_libro("L001", "El principito", "Antoine", "1943", "Novela")
    prestar_libro("L001", "Juan Pérez", "2026-06-01", "2026-06-15")
    mensaje = devolver_libro("L001")

    assert mensaje == "Libro devuelto con éxito."
    assert buscar_libro("L001")["estado"] == ESTADO_DISPONIBLE
    assert listar_prestamos() == ["No hay préstamos activos."]

def test_no_devolver_libro_inexistente():
    # Prueba el error al intentar devolver un código que no existe.
    limpiar()
    mensaje = devolver_libro("L999")

    assert mensaje == "Error: No existe un libro con el código L999."

def test_no_devolver_libro_disponible():
    # Prueba que no se pueda devolver un libro que no está prestado.
    limpiar()
    registrar_libro("L001", "El principito", "Antoine", "1943", "Novela")
    mensaje = devolver_libro("L001")

    assert mensaje == "Error: El libro L001 no está prestado."

def test_listar_libros_todos():
    # Prueba que listar sin filtro devuelva todos los libros.
    limpiar()
    registrar_libro("L001", "Libro 1", "Autor", "2000", "Drama")
    registrar_libro("L002", "Libro 2", "Autor", "2001", "Novela")

    assert len(listar_libros()) == 2

def test_listar_libros_por_estado():
    # Prueba que el filtro por estado devuelva solo los correspondientes.
    limpiar()
    registrar_libro("L001", "Libro 1", "Autor", "2000", "Drama")
    registrar_libro("L002", "Libro 2", "Autor", "2001", "Novela")
    prestar_libro("L001", "Juan", "2026-06-01", "2026-06-15")

    assert len(listar_libros(ESTADO_DISPONIBLE)) == 1
    assert len(listar_libros(ESTADO_PRESTADO)) == 1

def test_listar_prestamos():
    # Prueba que listar préstamos devuelva los activos correctamente.
    limpiar()
    registrar_libro("L001", "Libro 1", "Autor", "2000", "Drama")
    prestar_libro("L001", "Juan", "2026-06-01", "2026-06-15")

    assert len(listar_prestamos()) == 1

if __name__ == "__main__":
    test_registrar_libro()
    test_no_permite_codigo_repetido()
    test_año_invalido()
    test_prestar_libro()
    test_no_prestar_libro_inexistente()
    test_no_prestar_libro_ya_prestado()
    test_no_prestar_con_fecha_incorrecta()
    test_no_prestar_con_formato_fecha_invalido()
    test_devolver_libro()
    test_no_devolver_libro_inexistente()
    test_no_devolver_libro_disponible()
    test_listar_libros_todos()
    test_listar_libros_por_estado()
    test_listar_prestamos()
    limpiar()
    print("Todos los tests pasaron.")
