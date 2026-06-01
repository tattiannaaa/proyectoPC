# Biblioteca obligatorio

Proyecto simple en Python para gestionar libros y prestamos de una biblioteca.

## Archivos

- `biblioteca.py`: programa principal.
- `funciones_libros.py`: modulo con funciones para registrar y listar libros.
- `funciones_prestamos.py`: modulo con funciones para prestar, devolver y listar prestamos.
- `tests_biblioteca.py`: pruebas unitarias.

## Importante

El sistema guarda los datos en memoria usando un diccionario y una lista:

```python
libros = {}
prestamos = []
```

Por eso, los datos se mantienen mientras el programa esta abierto. Al cerrar el programa, se pierden.

## Ejecutar en modo interactivo

Desde la carpeta del proyecto:

```bash
python biblioteca.py
```

Ese modo es el mas recomendado para usar el programa, porque permite registrar, prestar, devolver y listar libros dentro de la misma ejecucion.

## Ejecutar comandos sueltos

Tambien se pueden ejecutar comandos con parametros:

```bash
python biblioteca.py registrar_libro L001 "El principito" "Antoine de Saint-Exupery" 1943 "Novela"
python biblioteca.py prestar_libro L001 "Juan Perez" 2026-06-01 2026-06-15
python biblioteca.py devolver_libro L001
python biblioteca.py listar_libros
python biblioteca.py listar_libros DISPONIBLE
python biblioteca.py listar_prestamos
```

Como no se usa archivo ni JSON, cada comando suelto empieza con la memoria vacia.

## Ejecutar tests

```bash
python -m unittest tests_biblioteca.py
```
