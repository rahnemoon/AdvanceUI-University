<template>
    <div class='column is-9 set-height mb-3'>
        <ScreenOnStream />
        <video ref="video_re" id="remote-video" autoplay></video>
        <button v-on:click='joinCall()'>start call</button>
        <!-- <video ref="video_lo" muted id="local-video" autoplay></video> -->
    </div>
</template>
<script>
import ScreenOnStream from './ScreenOnStream.vue'
const webSocketCall = new WebSocket("ws://127.0.0.1:3002");

let localStream
let peerCall
const id_call = 'Childish'



export default {
    name: 'Stream',
    props: {
        msg: String
    },
    components: {
        ScreenOnStream
    },
    methods: {
        joinCall() {
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

                peerCall = new RTCPeerConnection(configuration)
                peerCall.addStream(stream)
                console.log(peerCall)
                peerCall.onaddstream = (e) => {
                    this.$refs.video_re.srcObject = e.stream;
                }

                peerCall.onicecandidate = ((e) => {
                    if (e.candidate == null)
                        return
                    this.sendDataCall({
                        type: "send_candidate",
                        candidate: e.candidate
                    }, id_call)
                })
                console.log("join_call")
                this.sendDataCall({
                    type: "join_call"
                }, id_call)

            }, (error) => {
                console.log(error)
            })
        },

        handleSignallingCall(data) {
            switch (data.type) {
                case "offer":
                    console.log("offer")
                    peerCall.setRemoteDescription(data.offer)
                    this.createAndSendAnswerCall()
                    break
                case "candidate":
                    console.log("candidate")
                    peerCall.addIceCandidate(data.candidate)
            }

        },
        sendDataCall(data, id) {
            console.log(data);
            console.log(webSocketCall);
            data.username = id
            webSocketCall.send(JSON.stringify(data));
        },

        createAndSendAnswerCall() {
            peerCall.createAnswer((answer) => {
                peerCall.setLocalDescription(answer)
                console.log("send_answer")
                this.sendDataCall({
                    type: "send_answer",
                    answer: answer
                }, id_call)
            }, error => {
                console.log(error)
            })
        },


    },
    mounted() {
        webSocketCall.onmessage = (event) => {
            this.handleSignallingCall(JSON.parse(event.data))
        };
        webSocketScreen.onmessage = (event) => {
            this.handleSignallingScreen(JSON.parse(event.data))
        };
    },
}
</script>
<style scoped>
.home {
    background: #40E0D0;
}

#localVideo {
    visibility: hidden;
    opacity: 0;
}

video {
    background: black;
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border-radius: 10px;
    padding: 0;
}

.set-height {
    height: 75vh;
    position: relative;
}
</style>
