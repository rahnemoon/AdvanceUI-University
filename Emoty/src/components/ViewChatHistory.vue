<template>
    <div>
      <div class="message-body chat my-1">
          {{msg.txt}}
          <div class="columns">
            <div class="column">
            <img :src="set_img_directory(msg.emoji)">
            </div> 
            <div class="has-text-right is-size-7 has-text-grey-light column mr-3">{{msg.time}}</div> 
          </div>
        </div>
        <hr>
       </div>


</template>

<script>
export default {
  name: 'ViewChatHistory',
  props: {
    msg: Object
  },
  methods:{
      set_img_directory(assetName){      
      return  require('../assets/mini-emoji/'+assetName);
    },
  }
  }
</script>

<style scoped>
img {
  width: 20px;
  height: 20px;
}
div .message-body {
  padding-top: 0.7em;
  padding-bottom: 0.2em;

}
hr{
  border-top: 1px solid #b5b5b5;
  margin: 0 0.6em;
  padding: 0 1em;
}
.chat{
  padding: 0.75em 0.75em;
  border-width: 0 0 0 0;
}
</style>
