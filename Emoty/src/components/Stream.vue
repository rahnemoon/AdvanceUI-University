<template>

  <div class='column is-9 set-height mb-3'>
    
  <!-- <video id="localVideo" autoplay muted></video> !-->
    <ScreenOnStream/>
   <video id="remoteVideo" autoplay muted></video>
  </div>

</template>

<script>
import ScreenOnStream from './ScreenOnStream.vue'

export default {
  name: 'Stream',
  props: {
    msg: String
  },
  components:{
    ScreenOnStream
  },

}
</script>

<style scoped>
.home{
  background: #40E0D0;
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
