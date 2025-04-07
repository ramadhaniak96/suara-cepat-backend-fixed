from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask backend 👋"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files.get('audio')
    if not audio:
        return jsonify({"error": "No audio uploaded"}), 400
    return jsonify({"transcription": "Ini hasil transkripsi palsu 😄"}), 200

@app.route('/voiceover', methods=['POST'])
def voiceover():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    return jsonify({"audio_url": "https://fake.audio/output.mp3"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)