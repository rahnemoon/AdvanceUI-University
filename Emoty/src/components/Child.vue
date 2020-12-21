<template>
    <div style="padding-top: calc((100vh - 70vh)/2)">
     <!-- <video id="localVideo" autoplay muted></video> !-->
         <!--<video id="remoteVideo" autoplay muted></video>!-->

      <h1 class="circle"></h1>
    </div>

</template>

<script>
import io from 'socket.io-client';
export default {
  name: 'Child',
  props: {
    msg: String
  },

      created() {
      const socket = io.connect('http://127.0.0.1:5000');
      // eslint-disable-next-line
      socket.on('connect', function () {
            console.error('connected to webSocket');
            //sending to server
            socket.emit('lipsync', { data: 'I\'m connected!' });
      });
      //socket.on('update_on_layouts', (data) => {
        //    this.getAllLayouts();
          //  console.log(data);
      //    });
  },
}
</script>


<style scoped>
.circle { 
      width: 70vh; 
      height: 70vh; 
      background: white; 
      border-radius: 50%;
      margin: 0px auto;
      }
</style>
