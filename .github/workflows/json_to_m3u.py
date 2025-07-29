import json
import sys

def json_to_m3u(channels_file, playlist_file):
    with open(channels_file, "r") as f:
        channels = json.load(f)

    with open(playlist_file, "w") as m3u:
        m3u.write("#EXTM3U\n")
        for channel in channels:
            # Use `.get()` to safely access keys and provide default values
            channel_id = channel.get("id", "unknown")
            channel_name = channel.get("name", "Unknown Channel")
            channel_logo = channel.get("logo", "")
            channel_group = channel.get("group", "Misc")
            channel_url = channel.get("url", "")

            # Check if url is not empty before writing to file
            if channel_url:
                m3u.write(
                    f'#EXTINF:-1 tvg-id="{channel_id}" tvg-name="{channel_name}" '
                    f'tvg-logo="{channel_logo}" group-title="{channel_group}",{channel_name}\n'
                    f'{channel_url}\n'
                )
            else:
                print(f"Warning: Channel '{channel_name}' has no URL and will be skipped.")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = 'channels.json'
        output_file = 'playlist.m3u'

    json_to_m3u(input_file, output_file)
