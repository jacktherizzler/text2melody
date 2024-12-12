from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
headers = {"Authorization": "Bearer xxxxxxxx(your API key)xxxxxxxx"}

def query_musicgen(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # querying the music generation API
        audio_bytes = query_musicgen({"inputs": prompt})
        if audio_bytes is None:
            return jsonify({"error": "Failed to generate audio"}), 500

        # to save the audio file
        file_path = "static/generated_audio.wav"
        with open(file_path, "wb") as audio_file:
            audio_file.write(audio_bytes)

        return jsonify({"audio_url": file_path}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
