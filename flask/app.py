from flask import Flask, jsonify, render_template, json, request
from flask_cors import CORS
from google.cloud import texttospeech
import os
import subprocess

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./emoty-tts-key.json"

# sanity check route
def text_to_speech(message):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=message)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-H", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("Cache/output.wav", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')

    
def lip_sync():
    cmd = ["./Rhubarb_Lip_Sync/rhubarb","-o", "Cache/output.json", "Cache/output.wav", "-f", "json"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()

    with open("Cache/output.json", "r") as result:
        data = json.load(result)


@app.route('/text-input', methods=['POST'])
def text_input():
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        #response_obj["message"] = post_data["txt"]
        text_to_speech(post_data["txt"])
        lip_sync()

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

if __name__ == '__main__':
    app.run()
