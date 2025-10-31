from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "SOLTANI Gateway Server – active and ready."

@app.route('/tts', methods=['POST'])
def tts_gateway():
    data = request.json
    text = data.get("text", "")
    
    # شبیه‌سازی عملکرد Wondercraft TTS
    response = {
        "status": "ok",
        "input_text": text,
        "audio_url": f"https://api.wondercraft.ai/tts?text={text}"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)