<template>

  <div class='column is-9 set-height mb-3'>
    
  <!-- <video id="localVideo" autoplay muted></video> !-->
  <video id="remoteVideo" autoplay muted></video>
  </div>

</template>

<script>
export default {
  name: 'Stream',
  props: {
    msg: String
  },
  
}
</script>

<style scoped>
.home{
  background: #40E0D0;
}
video {
  background: white;
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
}
</style>
