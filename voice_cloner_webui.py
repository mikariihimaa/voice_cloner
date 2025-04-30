from flask import Flask, request, render_template_string, send_file
from TTS.api import TTS
import os
import time
import torch

# Lisää kaikki turvalliseksi sallitut XTTS-luokat
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.config.shared_configs import BaseDatasetConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs

torch.serialization.add_safe_globals([
    XttsConfig,
    BaseDatasetConfig,
    XttsAudioConfig,
    XttsArgs
])

# Mallin nimi
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = TTS(MODEL_NAME, gpu=False)

# Flask-sovellus
app = Flask(__name__)

# HTML-käyttöliittymä
HTML_TEMPLATE = '''
<!doctype html>
<title>Voice Cloner</title>
<h1>Voice Cloner Web UI</h1>
<form method=post enctype=multipart/form-data>
  <label>Enter text:</label><br>
  <textarea name=text rows=5 cols=60></textarea><br><br>
  <label>Upload voice sample (wav):</label>
  <input type=file name=voice><br><br>
  <input type=submit value=Generate>
</form>
{% if output_file %}
  <h2>Download cloned audio:</h2>
  <a href="/{{ output_file }}" download>{{ output_file }}</a>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    output_file = None
    if request.method == 'POST':
        text = request.form['text']
        voice = request.files['voice']
        ref_wav_path = "ref.wav"
        voice.save(ref_wav_path)

        print(f" > Teksti: {text}")
        print(f" > Ääninäyte tallennettu: {ref_wav_path}")

        timestamp = int(time.time())
        output_file = f"output_{timestamp}.wav"

        # Muunna teksti puheeksi
        tts.tts_to_file(
            text=text,
            speaker_wav=ref_wav_path,
            language="en",
            file_path=output_file
        )
        print(f"✅ Tallennettu tiedostoon: {output_file}")
        return render_template_string(HTML_TEMPLATE, output_file=output_file)

    return render_template_string(HTML_TEMPLATE, output_file=None)

@app.route('/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
