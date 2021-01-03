<template>
  <div class='set-size'>

    <video id="remoteVideo" autoplay muted></video>
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

      <button class="btn" @click="send_reaction('Anger')">
      <img src="../assets/mini-emoji/Anger.svg">
      </button>

      <button class="btn" @click="send_reaction('Fear')">
      <img src="../assets/mini-emoji/Fear.svg">
      </button>

      <button class="btn" @click="send_reaction('Anger')">
      <img src="../assets/mini-emoji/Anger.svg">
      </button>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ScreenOnStream',
  props: {
    msg: String
  },

  methods:{
      send_reaction(reaction){
      const url = "http://localhost:5000/selected_reaction";
      var msg = {reaction: reaction};
      axios.post(url, msg)
      .catch((error) => {console.log(error);});

    },

  },
}
</script>

<style scoped>

.btn{
      background-color: solid;
      border: 10px;
      position: absolute;
      z-index: 1;
      background: Transparent;
      border-radius: 50px;
  
}
.btn:focus{
      outline: 0;
      
}
.btn:hover{
      box-shadow: 0 0 4pt 1pt rgba(30,136,229 ,0.5);
      background: rgba(30,136,229 ,0.5);
      
}
.btn:active{
      outline:  0;
      box-shadow: 0 0 4pt 1pt rgba(30,136,229 ,0.3);
      background: rgba(30,136,229 ,0.8);
      
      
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
video {
      background: white;
      background-repeat: no-repeat;
      background-position: center;
      background-size: contain;

      box-sizing: border-box;
      border-radius: 10px;
      padding: 0;

      height:80%;
      width: 100%;
      border-radius: 50% / 100%;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
}
</style>
