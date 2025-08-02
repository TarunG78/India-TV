import requests
import re
import logging
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)

def fetch_m3u_data(url):
    """Función para obtener el contenido de un archivo M3U desde una URL."""
    logging.info(f"Fetching data from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        logging.error(f"Failed to fetch data: {response.status_code}")
        return None

def parse_m3u(data):
    """Función para analizar el contenido M3U y extraer información relevante."""
    logging.info("Parsing M3U data")
    lines = data.splitlines()
    streams = []
    current_stream = {}
    
    for line in lines:
        if line.startswith("#EXTINF:"):
            match = re.search(r'tvg-logo="([^"]+)" group-title="([^"]+)", (.+)', line)
            if match:
                current_stream['name'] = match.group(3).strip()
                current_stream['logo'] = match.group(1).strip()
                current_stream['group_title'] = match.group(2).strip()
        elif line.startswith("#EXTHTTP:"):
            current_stream['http'] = line.split(" ", 1)[1]
        elif line.startswith("http"):
            current_stream['url'] = line.strip()
            streams.append(current_stream)
            current_stream = {}

    return streams

def export_m3u(streams, path):
    """Función para exportar los streams a un archivo M3U."""
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    
    with open(path, 'w', encoding='utf-8') as file:
        for stream in streams:
            file.write(f'#EXTINF:-1 tvg-logo="{stream["logo"]}" group-title="{stream["group_title"]}", {stream["name"]}\n')
            file.write(f'#EXTHTTP:{stream["http"]}\n')
            file.write(f'{stream["url"]}\n')
    logging.info(f"Exported streams to {path}")

def main():
    url = "https://raw.githubusercontent.com/Raulpa78/m3u/refs/heads/main/artl.m3u"
    data = fetch_m3u_data(url)
    if data:
        streams = parse_m3u(data)
        for stream in streams:
            logging.info(f"Stream Name: {stream['name']}, URL: {stream['url']}, Logo: {stream['logo']}, Group: {stream['group_title']}, HTTP: {stream['http']}")
        # Exportar a archivo M3U
        export_path = "India-TV/Artl/artl.m3u"
        export_m3u(streams, export_path)

if __name__ == "__main__":
    main()