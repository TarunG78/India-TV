import json

def json_to_m3u(json_file, m3u_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        channels = json.load(f)

    m3u_lines = ["#EXTM3U"]
    for ch in channels:
        extinf = (
            f'#EXTINF:-1 tvg-id="{ch.get("id", "")}" '
            f'tvg-logo="{ch.get("logo_url", "")}" '
            f'group-title="",{ch.get("title", "")}'
        )
        m3u_lines.append(extinf)
        # Add additional info as comments
        if ch.get("license_url"):
            m3u_lines.append(f'#LICENSE-URL: {ch["license_url"]}')
        if ch.get("user_agent"):
            m3u_lines.append(f'#USER-AGENT: {ch["user_agent"]}')
        if ch.get("cookie"):
            m3u_lines.append(f'#COOKIE: {ch["cookie"]}')
        m3u_lines.append(ch.get("stream_url", ""))

    with open(m3u_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(m3u_lines))

if __name__ == "__main__":
    json_to_m3u("full_channels.json", "new_full_jio_zee.m3u")