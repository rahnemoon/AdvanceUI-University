<template>
    <div class='set-size'>
      <div class="oval has-background-white">
          <div class="circle">
        <video ref="video_screen" class="zoom mt-2" id="screenVideo" autoplay muted></video>
        </div>
      </div>

        <button class="btn" @click="send_reaction('Sad')" aria-label="Sad" data-microtip-position="left" role="tooltip">
            <img src="../assets/mini-emoji/Sad.svg" :class="[ sad_mini_emoji ? 'animation' : '' ]">
        </button>
        <button class="btn" @click="send_reaction('Happy')" aria-label="Happy" data-microtip-position="left" role="tooltip">
            <img src="../assets/mini-emoji/Happy.svg" :class="[ happy_mini_emoji ? 'animation' : '' ]" >
        </button>
        <button class="btn"  @click="send_reaction('Surprised')" aria-label="Surprised" data-microtip-position="left" role="tooltip">
            <img src="../assets/mini-emoji/Surprised.svg" :class="[ surprised_mini_emoji ? 'animation' : '' ]">
        </button>
        <button class="btn" @click="show_circle_emoji_childside()"  style="width: 50px; height: 50px;" aria-label="Toggle circle emojis" data-microtip-position="bottom" role="tooltip">
            <div v-if= "!toggle_state">
                <img src="../assets/mini-emoji/Toggle_off.svg">

            </div>
            <div v-else >
                <img src="../assets/mini-emoji/Toggle_on.svg">
            </div>

        </button>
        <button class="btn"  @click="send_reaction('Anger')" aria-label="Angry" data-microtip-position="right" role="tooltip">
            <img src="../assets/mini-emoji/Anger.svg" :class="[ anger_mini_emoji ? 'animation' : '' ]">
        </button>
        <button class="btn" :class="[ fear_mini_emoji ? 'animation' : '' ]" @click="send_reaction('Fear')" aria-label="Fear" data-microtip-position="right" role="tooltip">
            <img src="../assets/mini-emoji/Fear.svg" :class="[ fear_mini_emoji ? 'animation' : '' ]">
        </button>
        <button class="btn"  @click="send_reaction('Disgust')" aria-label="Disgust" data-microtip-position="right" role="tooltip">
            <img src="../assets/mini-emoji/Disgust.svg" :class="[ disgust_mini_emoji ? 'animation' : '' ]">
        </button>
    </div>
</template>
<script>


import axios from 'axios';
const webSocketScreen = new WebSocket("ws://127.0.0.1:3002");

let localStream
let peerScreen

export default {
    name: 'ScreenOnStream',
    props: {
        msg: String
    },

    methods: {
        receive_start_session() {
            this.$eventHub.$on('start_session', this.start_screenShare);
        },
        start_screenShare(msg){
            if (msg == 'start') {
            this.joinScreen()
        }
        },
        send_reaction(reaction) {

            const url = "http://localhost:5000/selected_reaction";
            var msg = { reaction: reaction };
            axios.post(url, msg)
                .catch((error) => { console.log(error); });

        this.sad_mini_emoji = true;
        this.happy_mini_emoji= true;
        this.surprised_mini_emoji= true;
        this.anger_mini_emoji= true;
        this.fear_mini_emoji= true;
        this.disgust_mini_emoji =true;

            switch (reaction) {
                case 'Anger':
                    this.anger_mini_emoji=false;
                    break;

                case 'Surprised':
                    this.surprised_mini_emoji=false;
                    break;

                case 'Sad':
                    this.sad_mini_emoji=false;
                    break;

                case 'Happy':
                    this.happy_mini_emoji=false;
                    break;

                case 'Fear':
                    this.fear_mini_emoji=false;
                    break;

                case 'Disgust':
                    this.disgust_mini_emoji=false;
            };

        },
        show_circle_emoji_childside() {
            const url = "http://localhost:5000/show_circle_emoji";
            var msg = { visibility: 'signal'};
            axios.post(url, msg)
                .catch((error) => { console.log(error); });

            this.toggle_state = !this.toggle_state;

        this.sad_mini_emoji = false;
        this.happy_mini_emoji= false;
        this.surprised_mini_emoji= false;
        this.anger_mini_emoji= false;
        this.fear_mini_emoji= false;
        this.disgust_mini_emoji =false;

        },
        joinScreen() {
            navigator.mediaDevices.getUserMedia({
                audio: false,
                video: true,
            }).then(stream => {
                localStream = stream
                let configuration = {
                    iceServers: [{
                        "urls": ["stun:stun.l.google.com:19302",
                            "stun:stun1.l.google.com:19302"
                        ]
                    }]
                }

                peerScreen = new RTCPeerConnection(configuration)
                peerScreen.addStream(stream)
                console.log(peerScreen)
                peerScreen.onaddstream = (e) => {
                    this.$refs.video_screen.srcObject = e.stream;
                }

                peerScreen.onicecandidate = ((e) => {
                    if (e.candidate == null)
                        return
                    this.sendDataScreen({
                        type: "send_candidate",
                        candidate: e.candidate
                    }, this.screen_room_id)
                })
                console.log("join_call")
                this.sendDataScreen({
                    type: "join_call"
                }, this.screen_room_id)

            }, (error) => {
                console.log(error)
            })
        },

        handleSignallingScreen(data) {
            switch (data.type) {
                case "offer":
                    console.log("offer")
                    peerScreen.setRemoteDescription(data.offer)
                    this.createAndSendAnswerScreen()
                    break
                case "candidate":
                    console.log("candidate")
                    peerScreen.addIceCandidate(data.candidate)
            }

        },

        createAndSendAnswerScreen() {
            peerScreen.createAnswer((answer) => {
                peerScreen.setLocalDescription(answer)
                console.log("send_answer")
                this.sendDataScreen({
                    type: "send_answer",
                    answer: answer
                }, this.screen_room_id)
            }, error => {
                console.log(error)
            })
        },

        sendDataScreen(data, id) {
            data.username = id
            webSocketScreen.send(JSON.stringify(data));
        },




    },
    mounted() {
        webSocketScreen.onmessage = (event) => {
            this.handleSignallingScreen(JSON.parse(event.data))
        };
    },
    created(){
        this.receive_start_session();
        var room_id = this.$route.params.room_id;
        if(room_id){
            console.log('room ' + room_id);
            this.screen_room_id = 'screen_' + room_id;
        }else{
            console.log('NO SCREEN ID');
        }
    },

    data(){
        return{
        toggle_state: false,
        sad_mini_emoji: false,
        happy_mini_emoji: false,
        surprised_mini_emoji: false,
        anger_mini_emoji: false,
        fear_mini_emoji: false,
        disgust_mini_emoji: false,
        screen_room_id: null,
        }
    }
}
</script>
<style scoped>

@keyframes taadaa {
  0% {
    opacity: 100%;
  }

  100% {
    opacity: 30%;
  }
}

.animation {
    -webkit-animation: taadaa 3.0s forwards; /* for less modern browsers */
    animation: taadaa 3.0s forwards;
}


.btn {
    background-color: solid;
    border: 10px;
    position: absolute !important;
    z-index: 1;
    background: Transparent;
    border-radius: 50px;
}

.btn:focus {
    outline: 0;

}

.btn:hover {
    box-shadow: 0 0 4pt 1pt rgba(30, 136, 229, 0.5);
    background: rgba(30, 136, 229, 0.5);

}

.btn:active {
    outline: 0;
    box-shadow: 0 0 4pt 1pt rgba(30, 136, 229, 0.3);
    background: rgba(30, 136, 229, 0.8);


}


.btn:nth-child(2) {
    bottom: 65%;
    left: -5%;
}

.btn:nth-child(3) {
    bottom: 28%;
    left: 5%;
}

.btn:nth-child(4) {
    bottom: 10%;
    left: 22%;
}

.btn:nth-child(5) {
    bottom: 0%;
    left: 44%;
}

.btn:nth-child(6) {
    bottom: 10%;
    left: 63%;
}

.btn:nth-child(7) {
    bottom: 28%;
    left: 80%;
}

.btn:nth-child(8) {
    bottom: 65%;
    left: 92%;
}

.set-size {
    height: 23vh;
    width: 35vw;
    background: Transparent;
    position: absolute;
    left: calc(39vw / 2);
}

@media only screen and (max-width:980px) {
    .set-size {
        width: 45vw;
        left: calc(28vw / 2);
    }
}

@media only screen and (max-width:680px) {
    .set-size {
        width: 60vw;
        left: calc(37vw / 2);
    }
}

@media only screen and (max-width:480px) {
    .set-size {
        width: 70vw;
        left: calc(27vw / 2);
    }
}
.zoom{
  -moz-transform:scale(7);
  -webkit-transform:scale(7);
  -o-transform:scale(7);
  -ms-transform:scale(7);
  transform:scale(7);
}
video {
    padding: 0;
    height: 45%;
    width: 100%;
}
.circle {
    width: 100px;
    height: 100px;
    background: rgb(255, 255, 255);
    border-radius: 50%;
    margin: 0px auto;
    overflow: hidden;

}
.oval{
    background: white;
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    overflow: hidden;

    position: absolute;
    border-radius: 50% / 100%;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    height: 80%;
    width: 100%;
}
</style>
