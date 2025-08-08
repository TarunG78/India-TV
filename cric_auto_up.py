import json
import os
import requests

# Obtener la URL desde la variable de entorno
url = os.getenv('JSON_API_URL')

# Comprobar si la URL se ha obtenido
if not url:
    print("Error: La URL del JSON no está definida.")
    exit(1)

# Obtener el contenido JSON desde la URL
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    json_data = response.json()  # Convertir la respuesta a JSON
    print(json_data)  # Agregar esta línea para imprimir el contenido
else:
    print(f"Error al obtener el archivo JSON: {response.status_code}")
    exit(1)  # Salir del script en caso de error

# Nombre del archivo de salida
output_file = 'cricautoupdate.m3u'

with open(output_file, 'w') as file:
    # Escribir la cabecera del archivo M3U
    file.write("#EXTM3U\n")
    
    # Iterar sobre los datos JSON
    for channel in json_data:
        # Extraer los detalles del canal
        name = channel.get('name')
        link = channel.get('link')
        referer = channel.get('referer')
        origin = channel.get('origin')
        
        # Escribir la información del canal en el formato M3U
        file.write(f"#EXTINF:-1 tvg-id=\"{channel['id']}\" tvg-logo=\"{channel['logo']}\" group-title=\"Channels\", {name}\n")
        # Incluir Referer y Origin como comentarios
        file.write(f"# Referer: {referer}\n")
        file.write(f"# Origin: {origin}\n")
        file.write(f"{link}\n")


print(f"Archivo {output_file} creado exitosamente.")
