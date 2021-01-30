from flask import Flask, jsonify, render_template, json, request
from flask_cors import CORS
from google.cloud import texttospeech
import os
import subprocess
from flask_socketio import SocketIO
from flask_socketio import send, emit
import platform

DEBUG = True

# These global variables are used to check whether corresponding files
# have been sent or not. Because SocketIO sends file periodically by using
# these variables we are preventing repetitive sending of files.

global CHECK_FILES_SEND
CHECK_FILES_SEND = False

global SELECTED_EMOTION
SELECTED_EMOTION = ''

global SELECTED_QUICK_REACTION
SELECTED_QUICK_REACTION = ''

global CHECK_EMOTION_SEND
CHECK_EMOTION_SEND = False

global CHECK_QUICK_REACTION_SEND
CHECK_QUICK_REACTION_SEND = False

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app, engineio_logger=True)
socketio.init_app(app, cors_allowed_origins="*")

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app, resources={r'/*': {'origins': '*'}})

# Initialization of google token to access tts service
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./emoty-tts-key.json"

# List of quick reactions that are supposed to be sent to therapist side
# during the render of interface
quick_reactions = {
    'Hello': {
        'id': '0',
        'animation': 'Happy',
        'emoji': 'Happy.svg',
    },

    'How are you?': {
        'id': '1',
        'animation': 'Neutral',
        'emoji': 'Neutral.svg',
    },

    'Nice job!': {
        'id': '2',
        'animation': 'Happy',
        'emoji': 'Happy.svg',
    },

    "I'm sorry.": {
        'id': '3',
        'animation': 'Sad',
        'emoji': 'Sad.svg',
    },

    "I couldn't hear you, can you repeat?": {
        'id': '4',
        'animation': 'Neutral',
        'emoji': 'Neutral.svg',
    },

    'Try again!': {
        'id': '5',
        'animation': 'Neutral',
        'emoji': 'Neutral.svg',
    },
}

# function that receives a text message and returns writes
# generated audio by google tts in default directory


def text_to_speech(message):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=message)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-H",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Note, in order to change the speed of generated audio
    # speaking_rate has to be modified

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=0.7
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("Cache/output.wav", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')

    global CHECK_FILES_SEND
    CHECK_FILES_SEND = True

# lip_sync function generates visemes (in default directory )for the corresponding
# generated audio using Rhubarb_Lip_Sync package


def lip_sync():
    # notice Rhubarb_Lip_Sync package is platform dependent
    # so, here we take care of platform to use the proper version
    plat = platform.system()
    path = ''
    if plat == 'Darwin':
        path = "./Rhubarb_Lip_Sync/rhubarb-lip-sync-1.10.0-osx/rhubarb"
    elif plat == 'Linux':
        path = "./Rhubarb_Lip_Sync/rhubarb-lip-sync-1.10.0-linux/rhubarb"
    elif plat == 'Windows':
        path = "./Rhubarb_Lip_Sync/rhubarb-lip-sync-1.10.0-win32/rhubarb.exe"

    cmd = [path, "-o", "Cache/output.json", "Cache/output.wav", "-f", "json"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    out, err = p.communicate()

    with open("Cache/output.json", "r") as result:
        data = json.load(result)


# API receives message with selected emotion from therapist side
@app.route('/text-input', methods=['POST'])
def text_input():
    global SELECTED_EMOTION
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        SELECTED_EMOTION = post_data['emoji'].split('.')[0]
        text_to_speech(post_data["txt"])
        lip_sync()

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# API answers the get request with list of quick
# reactions(specified in dictionary above) to therapist side


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

# API receives submitted quick reaction form therapist


@app.route('/submitted_qr', methods=['POST'])
def receive_quick_reaction():
    global SELECTED_QUICK_REACTION
    global CHECK_QUICK_REACTION_SEND
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        SELECTED_QUICK_REACTION = post_data
        CHECK_QUICK_REACTION_SEND = True

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# API receives selected reaction(full body emotion recreation)
# form therapist which are shown on floating panel of stream


@app.route('/selected_reaction', methods=['POST'])
def receive_reaction():
    global CHECK_EMOTION_SEND
    global SELECTED_EMOTION
    response_obj = {"status": "successful"}
    if request.method == "POST":
        post_data = request.get_json()
        SELECTED_EMOTION = post_data['reaction']
        CHECK_EMOTION_SEND = True

    else:
        response_obj["status"] = "failed"

    return jsonify(response_obj)

# reading json file(visemes)


def read_lips_sync():
    with open('Cache/output.json', 'r') as file:
        return json.load(file)

# reading wav audio file(generated audio)


def read_generated_audio():
    with open('Cache/output.wav', 'rb') as audio:
        data = audio.read()
        return data


# socket for sending files(audio, visemes, emotions)
@socketio.on('send_file', namespace='/lips')
def send_json(message):
    global CHECK_FILES_SEND
    global SELECTED_EMOTION
    global CHECK_EMOTION_SEND
    global CHECK_QUICK_REACTION_SEND
    global SELECTED_QUICK_REACTION

    # this condition handles emitting of a audio, visemes and emotion
    if CHECK_FILES_SEND == True:
        lips_json = json.dumps(read_lips_sync())
        audio = read_generated_audio()
        emit('send_json', lips_json)
        emit('send_audio', audio)
        emit('send_emotion', SELECTED_EMOTION)

        CHECK_FILES_SEND = False

    # this condition handles emitting of full body emotion recreation
    if CHECK_EMOTION_SEND == True:
        emit('full_emotion_recreation', SELECTED_EMOTION)
        CHECK_EMOTION_SEND = False

    # this condition handles emitting of a audio, visemes and emotion
    # for selected quick reaction
    if CHECK_QUICK_REACTION_SEND == True:
        idd = SELECTED_QUICK_REACTION['id']
        emotion = quick_reactions[SELECTED_QUICK_REACTION['key']]['animation']

        with open("QuickReactions/" + str(idd) + ".wav", "rb") as out:
            audio_q = out.read()

        with open("QuickReactions/" + str(idd) + ".json", "r") as lips:
            lipsync_q = lips.read()

        emit('send_json', lipsync_q)
        emit('send_audio', audio_q)
        emit('send_emotion', emotion)

        CHECK_QUICK_REACTION_SEND = False


if __name__ == '__main__':
    socketio.run(app, debug=True)
