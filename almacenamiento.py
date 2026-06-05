# Modulo para guardar y cargar los datos de la biblioteca.
# Los datos se guardan en un archivo JSON para que no se pierdan cuando el programa termina.

import json

ARCHIVO_DATOS = "datos.json"

def cargar_datos():
    # Carga los datos del archivo JSON.
    # Si el archivo no existe, retorna estructuras vacías.
    try:
        archivo = open(ARCHIVO_DATOS, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos
    except FileNotFoundError:
        return {"libros": {}, "prestamos": []}

def guardar_datos(datos):
    # Guarda los datos en el archivo JSON.
    archivo = open(ARCHIVO_DATOS, "w", encoding="utf-8")
    json.dump(datos, archivo, indent=2, ensure_ascii=False)
    archivo.close()
