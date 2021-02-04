<template>
    <div class='column is-9 set-height mb-3'>
        <ScreenOnStream />
        <video ref="video_re" id="remote-video" autoplay></video>
    </div>
</template>
<script>
import ScreenOnStream from './ScreenOnStream.vue'

const webSocketCall = new WebSocket("ws://127.0.0.1:3002");

let localStream
let peerCall

export default {
    name: 'Stream',
    props: {
        msg: String
    },
    components: {
        ScreenOnStream
    },
    methods: {
        receive_start_session() {
            this.$eventHub.$on('start_session', this.start_call);
        },
        start_call(msg) {
            if (msg == 'start') {
                this.joinCall()
            }
        },
        joinCall() {
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
                    }, this.call_room_id)
                })
                console.log("join_call")
                this.sendDataCall({
                    type: "join_call"
                }, this.call_room_id)

            }, (error) => {
                console.log(error)
            })
        },

        handleSignallingCall(data) {
            switch (data.type) {
                case "offer":
                    peerCall.setRemoteDescription(data.offer)
                    this.createAndSendAnswerCall()
                    break
                case "candidate":
                    peerCall.addIceCandidate(data.candidate)
            }

        },
        sendDataCall(data, id) {
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
                }, this.call_room_id)
            }, error => {
                console.log(error)
            })
        },


    },
    mounted() {
        webSocketCall.onmessage = (event) => {
            this.handleSignallingCall(JSON.parse(event.data))
        };
        this.receive_start_session();
    },
    created() {
        var room_id = this.$route.params.room_id;
        if (room_id) {
            console.log('room ' + room_id);
            this.call_room_id = 'child_' + room_id;
        } else {
            console.log('NO CALL ID');
            this.$alert("Please eneter the name of the room in the address bar", "Error", "error", {
                confirmButtonText: "Got it!"
            });
        }
    },
    data() {
        return {
            call_room_id: null,
        }
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
