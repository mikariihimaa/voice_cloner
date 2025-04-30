import os
import torch
from flask import Flask, request, render_template, send_file
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig

torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    XttsArgs,
    BaseDatasetConfig
])

app = Flask(__name__)
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = TTS(MODEL_NAME, gpu=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        file = request.files["audio"]

        # Tallenna ladattu tiedosto
        speaker_path = "speaker.wav"
        file.save(speaker_path)

        output_path = "output.wav"

        tts.tts_to_file(
            text=text,
            speaker_wav=speaker_path,
            language="en",
            file_path=output_path
        )

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
