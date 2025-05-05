import json
import os

# Ruta del archivo JSON
ruta_archivo = r"autos_deportivos.json"

# Verificamos si el archivo existe
if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
    try:
        # Abrimos el archivo JSON
        with open(ruta_archivo, "r") as archivo:
            datos = json.load(archivo)
        
        # Mostrar los datos leídos del archivo
        print(json.dumps(datos, indent=4))  # Imprime el JSON de manera bonita y legible

    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {e}")
else:
    print("El archivo no existe o está vacío.")
