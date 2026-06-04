# Biblioteca obligatorio

Proyecto simple en Python para gestionar libros y prestamos de una biblioteca.

## Archivos

- `biblioteca.py`: programa principal.
- `libros.py`: modulo con funciones para registrar y listar libros.
- `prestamos.py`: modulo con funciones para prestar, devolver y listar prestamos.
- `almacenamiento.py`: modulo con funciones para guardar y cargar datos desde archivos de texto.
- `tests.py`: pruebas del programa.

## Importante

El sistema guarda los libros en `libros.txt` y los prestamos en `prestamos.txt`.

Cada libro se guarda en una linea con este formato:

```text
codigo;titulo;autor;ano;genero;estado
```

Cada prestamo se guarda en una linea con este formato:

```text
codigo_libro;persona;fecha_prestamo;fecha_devolucion
```

## Ejecutar comandos

Desde la carpeta del proyecto:

Para ver la ayuda del programa:

```bash
python biblioteca.py
python biblioteca.py ayuda
```

Comandos disponibles:

```bash
python biblioteca.py registrar_libro L001 "El principito" "Antoine de Saint-Exupery" 1943 "Novela"
python biblioteca.py prestar_libro L001 "Juan Perez" 2026-06-01 2026-06-15
python biblioteca.py devolver_libro L001
python biblioteca.py listar_libros
python biblioteca.py listar_libros DISPONIBLE
python biblioteca.py listar_libros PRESTADO
python biblioteca.py listar_prestamos
```

## Ejecutar tests

```bash
python tests.py
```
