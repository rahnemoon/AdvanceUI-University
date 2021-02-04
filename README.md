# Emoty [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) ![](https://erguotou520.github.io/vue-version-badge/vue2.x.svg)
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
