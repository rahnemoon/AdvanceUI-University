# Emoty [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) ![](https://erguotou520.github.io/vue-version-badge/vue2.x.svg)
**Emoty** provides a new conversational experience for therapists and Children with ***neurodevelopmental disability (NDD)*** problems. This system helps children with such conditions to develop and cultivate their emotional abilities by offering a friendly and enjoyable environment. The therapist communicates with the child as an animated character via the ***wizard of Oz*** scenario.


## Running the Project


### API

- Create a Python virtual environment and execute the following command
```
virtualenv NAME_OF_ENV && source NAME_OF_ENV/bin/activate
```
- Install Python required packages (Flask, SocketIO, ...)
```
cd flask
pip install -r requirments.txt
```
***Note:*** in case if Python virtual environment is not installed, run the subsequent command
```
pip install virtualenv
```

- Run the Flask Server as API of the project by

```
python app.py
```
### Front End

- Install the NPM package manager and NodeJS base on your OS. Next, run the command to install required packages (Vuejs, ...) to Run the FrontEnd of the project
```
cd Emoty
npm install
```
- Execute the command to run the serving server
```
npm run serve
```

### Signaling Server *(for WebRTC Connection)*

- Having installed before the NodeJS, NPM and required packages, execute the command to run the server.
```
node server.js
```

## [License](LICENSE)

## Team of contributors
- Esteva, Clara - clara.esteva@mail.polimi.it
- Guzey, Ceren - ceren.guzey@mail.polimi.it
- Molaei, Amirsalar - Amirsalar.molaei@mail.polimi.it
- Rahnemoon, Erfan - erfan.rahnemoon@mail.polimi.it

## References
- Jennifer L. Scotland, Karen McKenzie, Jill Cossar, Aja Murray, Amanda Michie, Recognition of facial expressions of emotion by adults with intellectual disability: Is there evidence for the emotion specificity hypothesis?, Research in  Developmental Disabilities Volume 48
- Understanding emotions from standardized facial expressions in autism and normal development, Fulvia Castelli, California Institute of Technology, USA, autism © 2005 SAGE Publications and The National Autistic Society Vol 9(4)
- AW, Young & Perrett, David & Calder, A. & Sprengelmeyer, Reiner & Ekman, P.. (2002). Facial expressions of emotion: Stimuli and tests (FEEST). Thames Valley Test Company (TVTC).
- Fabio Catania, Nicola Di Nardo, Franca Garzotto, Daniele Occhiuto, Emoty: An Emotionally Sensitive Conversational Agent for People with Neurodevelopmental Disorders, Proceedings of the 52nd Hawaii International Conference on System Sciences, 2019
- Aslam MM (2006). "Are You Selling the Right Colour? A Cross-cultural Review of Colour as a Marketing Cue". Journal of Marketing Communications. 15-30
- Elliot AJ (2015-04-02). "Color and psychological functioning: a review of theoretical and empirical work". Frontiers in Psychology. 6: 368.

- [Rhubarb Lip Sync](https://github.com/DanielSWolf/rhubarb-lip-sync)
- [Google TTS](https://cloud.google.com/text-to-speech/docs)
	- ***NOTE:*** The Google cloud credential should be replaced by your own in the flask/emoty-tts-key.json file.
