from flask import Flask, Response
import os

app = Flask(__name__)

# 👉 Живая ссылка на канал (пока вставляем вручную)
ANIMAL_PLANET_URL = "https://s.viks.tv/CHyyj6YQFVqh_xsh6r68LQ/600/1758492698/index.m3u8"

@app.route("/")
def index():
    return "IPTV Proxy работает! Перейди на /animalplanet.m3u8"

@app.route("/animalplanet.m3u8")
def animalplanet():
    # M3U плейлист, который телевизор поймет
    m3u8_content = f"""#EXTM3U
#EXTINF:-1,Animal Planet
{ANIMAL_PLANET_URL}
"""
    return Response(m3u8_content, mimetype="application/vnd.apple.mpegurl")

if __name__ == "__main__":
    # Render подставит свой порт через переменную окружения PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
