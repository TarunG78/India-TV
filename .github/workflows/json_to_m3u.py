import json
import sys

def json_to_m3u(channels.json, playlist.m3u):
    with open(json_file, "r") as f:
        channels = json.load(f)

    with open(m3u_file, "w") as m3u:
        m3u.write("#EXTM3U\n")
        for channel in channels:
            m3u.write(
                f'#EXTINF:-1 tvg-id="{channel["id"]}" tvg-name="{channel["name"]}" tvg-logo="{channel["logo"]}" group-title="{channel["group"]}",{channel["name"]}\n'
                f'{channel["url"]}\n'
            )

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = 'channels.json'
        output_file = 'playlist.m3u'
    json_to_m3u(channels.json, playlist.m3u)
