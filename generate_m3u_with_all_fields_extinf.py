import json

def json_to_m3u(json_file, m3u_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        channels = json.load(f)

    m3u_lines = ["#EXTM3U"]
    for ch in channels:
        # Prepare custom attributes (escape quotes if needed)
        license_url = ch.get("license_url", "")
        user_agent = ch.get("user_agent", "")
        cookie = ch.get("cookie", "")
        extinf = (
            f'#EXTINF:-1 tvg-id="{ch.get("id", "")}" '
            f'tvg-logo="{ch.get("logo_url", "")}" '
            f'group-title=""'
            f' license_url="{license_url}"'
            f' user_agent="{user_agent}"'
            f' cookie="{cookie}",{ch.get("title", "")}'
        )
        m3u_lines.append(extinf)
        m3u_lines.append(ch.get("stream_url", ""))

    with open(m3u_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(m3u_lines))

if __name__ == "__main__":
    json_to_m3u("full_channels.json", "new_full_jio_zee.m3u")