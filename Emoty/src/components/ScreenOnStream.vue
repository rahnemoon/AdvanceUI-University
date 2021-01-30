<template>
    <div class='set-size'>
      <!-- <div class="zoom"> -->
        <video ref="video_screen" id="screenVideo" autoplay muted></video>
      <!-- </div> -->
        <!-- work on zooming on emoty !-->
        <button class="btn" @click="send_reaction('Sad')">
            <img src="../assets/mini-emoji/Sad.svg">
        </button>
        <button class="btn" @click="send_reaction('Happy')">
            <img src="../assets/mini-emoji/Happy.svg">
        </button>
        <button class="btn" @click="send_reaction('Surprised')">
            <img src="../assets/mini-emoji/Surprised.svg">
        </button>
        <button class="btn" @click="show_circle_emoji_childside()" style="width: 100px; height: 100px;">
            <img src="../assets/unicorn.svg">
        </button>
        <button class="btn" @click="send_reaction('Anger')">
            <img src="../assets/mini-emoji/Anger.svg">
        </button>
        <button class="btn" @click="send_reaction('Fear')">
            <img src="../assets/mini-emoji/Fear.svg">
        </button>
        <button class="btn" @click="send_reaction('Disgust')">
            <img src="../assets/mini-emoji/Disgust.svg">
        </button>
    </div>
    </div>
</template>
<script>
import axios from 'axios';
const webSocketScreen = new WebSocket("ws://127.0.0.1:3002");

let localStream
let peerScreen
const id_screen = 'screen'

export default {
    name: 'ScreenOnStream',
    props: {
        msg: String
    },

    methods: {
        receive_start_session() {
            this.$eventHub.$on('start_session', this.start_screenShare);
            console.log('start_session')

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

        },
        show_circle_emoji_childside() {
            const url = "http://localhost:5000/show_circle_emoji";
            var msg = { visibility: 'signal'};
            axios.post(url, msg)
                .catch((error) => { console.log(error); });

        },
        joinScreen() {
            navigator.mediaDevices.getUserMedia({
                audio: false,
                video: true,
            }).then(stream => {
                localStream = stream
                // this.$refs.video_lo.srcObject = stream;

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
                    }, id_screen)
                })
                console.log("join_call")
                this.sendDataScreen({
                    type: "join_call"
                }, id_screen)

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
                }, id_screen)
            }, error => {
                console.log(error)
            })
        },

        sendDataScreen(data, id) {
            console.log(data);
            console.log(webSocketScreen);
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
    }
}
</script>
<style scoped>
.btn {
    background-color: solid;
    border: 10px;
    position: absolute;
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
    bottom: 25%;
    left: 10%;
}

.btn:nth-child(4) {
    bottom: 10%;
    left: 31%;
}

.btn:nth-child(5) {
    bottom: 10%;
    left: 54%;
}

.btn:nth-child(6) {
    bottom: 25%;
    left: 75%;
}

.btn:nth-child(7) {
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
  -moz-transform:scale(3);
  -webkit-transform:scale(3);
  -o-transform:scale(3);
  -ms-transform:scale(3);
  transform:scale(3);
}
video {

    /*transform: translate(0%, 0%);*/
    /*zoom: 500%;*/
    background: white;
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;

    box-sizing: border-box;
    border-radius: 10px;
    padding: 0;

    height: 80%;
    width: 100%;
    border-radius: 50% / 100%;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>
