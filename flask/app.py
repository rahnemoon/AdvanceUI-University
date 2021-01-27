from flask import Flask, jsonify, render_template, json, request
from flask_cors import CORS
from google.cloud import texttospeech
import os
import subprocess
from flask_socketio import SocketIO
from flask_socketio import send, emit

#import socketio
#from wsgi import app
# configuration
DEBUG = True

global CHECK_FILES_SEND 
CHECK_FILES_SEND = False

global SELECTED_EMOTION 
SELECTED_EMOTION = ''

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app, engineio_logger=True)
socketio.init_app(app, cors_allowed_origins="*")
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./emoty-tts-key.json"

quick_reactions ={
    'Greetings': {
        'id': '0',
        'sound': '',
        'lip_sync': '',
        'animation': '',
        'emoji': 'Happy.svg',
    },

    'What popping': {
        'id': '1',
        'sound': '',
        'lip_sync': '',
        'animation': '',
        'emoji': 'Sad.svg',
    },

    'Nice job!': {
        'id': '2',
        'sound': '',
        'lip_sync': '',
        'animation': '',
        'emoji': 'Surprised.svg',
    },

    'Hang in there': {
        'id': '3',
        'sound': '',
        'lip_sync': '',
        'animation': '',
        'emoji': 'Fear.svg',
    },
}

# sanity check route
def text_to_speech(message):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=message)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-H", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=0.8
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("Cache/output.wav", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')

    global CHECK_FILES_SEND 
    CHECK_FILES_SEND = True

def lip_sync():
    cmd = ["./Rhubarb_Lip_Sync/rhubarb","-o", "Cache/output.json", "Cache/output.wav", "-f", "json"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()

    with open("Cache/output.json", "r") as result:
        data = json.load(result)


# receives message with selected emotion from therapist
@app.route('/text-input', methods=['POST'])
def text_input():
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        global SELECTED_EMOTION
        SELECTED_EMOTION = post_data['emoji'].split('.')[0]
        #response_obj["message"] = post_data["txt"]
        text_to_speech(post_data["txt"])
        lip_sync()

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# send list of quick reactions to therapist
@app.route('/quick-re', methods=['GET'])
def quick_reactions_send():
    response_obj = {"status": "successful"}
    if request.method == "GET":
        lists = []
        for k in quick_reactions:
            lists.append({
                'id': quick_reactions[k]['id'],
                'key': k,
                'emoji': quick_reactions[k]['emoji']
            })
        response_obj["re_list"] = lists

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# receive submitted quick reaction form therapist
@app.route('/submitted_qr', methods=['POST'])
def receive_quick_reaction():
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        # load from cache
        print("selected raction: " + str(post_data))

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# receive selected reaction form therapist which are shown on floating panel of stream
@app.route('/selected_reaction', methods=['POST'])
def receive_reaction():
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        print("selected raction: " + str(post_data))

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# read json file
def read_lips_sync():
    with open('Cache/output.json', 'r') as file:
        return json.load(file)

# read wav audio file 
def read_generated_audio():
    with open('Cache/output.wav', 'rb') as audio:
        data = audio.read()
        return data


# socket for sending audio and json     
@socketio.on('send_file', namespace='/lips')
def send_json(message):
    global CHECK_FILES_SEND
    global SELECTED_EMOTION

    if CHECK_FILES_SEND == True:
        lips_json = json.dumps(read_lips_sync())
        audio = read_generated_audio()
        emit('send_json', lips_json)
        emit('send_audio', audio)
        emit('send_emotion', SELECTED_EMOTION)

        CHECK_FILES_SEND = False
        print("Files are emitted.")
    #socketio.sleep(0)
if __name__ == '__main__':
    socketio.run(app, debug=True)
    #app.run()
    #sio = socketio.Server()
    #app = socketio.WSGIApp(sio, app)
