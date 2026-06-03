# Almacenamos todos los libros del sistema y cada libro es un diccionario con sus atributos
libros = []

# Recibe los datos del libro y lo registra en el sistema
def registrar_libro(codigo, titulo, autor, año, genero):
    """
    Registra un nuevo libro en el sistema.
    El estado inicial siempre es DISPONIBLE.
    """
    # Recorremos la lista para verificar que no exista un libro con el mismo código
    for libro in libros:
        if libro["codigo"] == codigo:
            print("Error: Ya existe un libro con el código", codigo)
            return

    # Creamos el diccionario con los datos del libro
    nuevo_libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "genero": genero,
        "estado": "DISPONIBLE"
    }

    # Se agrega a la lista
    libros.append(nuevo_libro)
    print("Libro registrado con éxito.")

# Recorre la lista e imprime cada libro, si no se indica estado, lista todos
def listar_libros(estado=None):
    """
    Lista los libros del sistema.
    Si se indica un estado (DISPONIBLE o PRESTADO), filtra por ese estado.
    Si no se indica estado, lista todos.
    """
    # Verifica que haya libros cargados
    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    for libro in libros:
        # Si se pidio filtrar por estado, salteamos los que no coinciden
        if estado != None and libro["estado"] != estado:
            continue
        print("Código:", libro["codigo"],
              "| Título:", libro["titulo"],
              "| Autor:", libro["autor"],
              "| Año:", libro["año"],
              "| Género:", libro["genero"],
              "| Estado:", libro["estado"])

def buscar_libro(codigo):
    """
    Busca un libro por su código y lo retorna.
    Si no existe, retorna None.
    """
    for libro in libros:
        if libro["codigo"] == codigo:
            return libro

    return None
