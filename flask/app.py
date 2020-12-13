from flask import Flask, jsonify, render_template, url_for, json
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
def text_to_speech():
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text="hello erfan, how are you doing, i hope that i can satisfy your needs, come on man let's do it, i'm hornny")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-H", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("Cache/output.wav", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')
    
    return jsonify("test")
    

@app.route('/', methods=['GET'])
def lip_sync():
    text_to_speech()
    cmd = ["./Rhubarb_Lip_Sync/rhubarb","-o", "Cache/output.json", "Cache/output.wav", "-f", "json"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()

    with open("Cache/output.json", "r") as result:
        data = json.load(result)

    return jsonify(data)

if __name__ == '__main__':
    app.run()
