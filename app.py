from flask import Flask, request, jsonify
from flask_cors import CORS
from ytmusicapi import YTMusic

app = Flask(__name__)
CORS(app)  # Enables CORS for all domains

ytmusic = YTMusic()

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify([])

    search_results = ytmusic.search(query, filter='songs')
    songs = []

    for song in search_results:
        songs.append({
            'title': song['title'],
            'artist': song['artists'][0]['name'] if song['artists'] else '',
            'album': song['album']['name'] if song.get('album') else '',
            'duration': song['duration'],
            'videoId': song['videoId'],
            'thumbnail': song['thumbnails'][-1]['url']
        })

    return jsonify(songs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
