<template>

  <div class='column is-9 set-height mb-3'>
    
    <ScreenOnStream/>
    
    <video ref="video_re" id="remote-video" autoplay></video>
        <button v-on:click='joinCall()'>start call</button>

    <video ref="video_lo" muted id="local-video" autoplay></video>

  </div>

</template>

<script>
import ScreenOnStream from './ScreenOnStream.vue'
const webSocket = new WebSocket("ws://127.0.0.1:3002");
let localStream
let peerConn
const therapist_id = 'Childish'


export default {
  name: 'Stream',
  props: {
    msg: String
  },
  components:{
    ScreenOnStream
  },
  methods:{

    handleSignallingData(data) {
    switch (data.type) {
        case "offer":
            console.log("offer")
            peerConn.setRemoteDescription(data.offer)
            this.createAndSendAnswer()
            break
        case "candidate":
            console.log("candidate")
            peerConn.addIceCandidate(data.candidate)
    }

  },
      sendData(data) {
        console.log(data);
      console.log(webSocket);
      data.username = therapist_id
      
      //webSocket.addEventListener('open',  (event) =>{
      webSocket.send(JSON.stringify(data));
      //});
      
      
    },

    createAndSendAnswer () {
    peerConn.createAnswer((answer) => {
        peerConn.setLocalDescription(answer)
        console.log("send_answer")
        this.sendData({
            type: "send_answer",
            answer: answer
        })
    }, error => {
        console.log(error)
    })
},

  joinCall() {
    navigator.mediaDevices.getUserMedia({
        audio: false,
        video: true,
    }).then(stream => {
        localStream = stream
          this.$refs.video_lo.srcObject = stream;

        let configuration = {
            iceServers: [
                {
                    "urls": ["stun:stun.l.google.com:19302",
                    "stun:stun1.l.google.com:19302"]
                }
            ]
        }

        peerConn = new RTCPeerConnection(configuration)
        peerConn.addStream(stream)
        console.log(peerConn)
        peerConn.onaddstream = (e) => {
            
        this.$refs.video_re.srcObject = e.stream;

        }

        peerConn.onicecandidate = ((e) => {
            if (e.candidate == null)
                return

            this.sendData({
                type: "send_candidate",
                candidate: e.candidate
            })
        })
        console.log("join_call")
        this.sendData({
            type: "join_call"
        })

    }, (error) => {
        console.log(error)
    })
},


  },
  mounted(){
    webSocket.onmessage = (event) => {
    this.handleSignallingData(JSON.parse(event.data))
      };
      this.joinCall();
  },
}
</script>

<style scoped>
.home{
  background: #40E0D0;
}
#localVideo{
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
