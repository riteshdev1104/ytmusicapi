from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic()

@app.route('/search')
def search_music():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Missing search query'}), 400

    results = ytmusic.search(query, filter="songs", limit=10)

    simplified = []
    for song in results:
        simplified.append({
            "title": song.get("title"),
            "videoId": song.get("videoId"),
            "duration": song.get("duration"),
            "artist": ', '.join([a["name"] for a in song.get("artists", [])]),
            "album": song.get("album", {}).get("name"),
            "thumbnail": song.get("thumbnails", [{}])[-1].get("url")
        })

    return jsonify(simplified)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)