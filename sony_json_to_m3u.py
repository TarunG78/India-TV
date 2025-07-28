import json

def json_to_m3u(json_file, m3u_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        channels = json.load(f)
    with open(m3u_file, 'w', encoding='utf-8') as f:
        f.write('#EXTM3U\n')
        for ch in channels:
            name = ch.get("title", "")
            logo = ch.get("logo", "")
            group = ch.get("genre", "")
            url = ch.get("m3u8", "")
            lang = ch.get("language", "")
            extinf = (
                f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}" tvg-language="{lang}",{name}\n'
            )
            f.write(extinf)
            f.write(f'{url}\n')

if __name__ == "__main__":
    json_to_m3u('sony_channels.json', 'sony_playlist.m3u')