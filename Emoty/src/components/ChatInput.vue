<template>
  <div class='column is-9'>
      <div class="control textarea-container has-fixed-size">
        <textarea class="textarea" placeholder="Text input" rows="2" v-model="input_txt"></textarea>
        <span class="mr-5 mt-4" v-on:click="on_submit()">
        <i class="fas fa-2x fa-paper-plane"></i>
        </span>
      </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatInput',
  props: {
    msg: String
  },
  methods: {
    send_message(msg){
      const url = "http://localhost:5000/text-input";
      axios.post(url, msg)
      .catch((error) => {console.log(error);});
    },
    on_submit(){
      const msg = {
      txt: this.input_txt
      };
      console.log(msg);
      this.send_message(msg)
    }  
  },
  data: function(){
    return{
      input_txt: null
    }
  },
}
</script>

<style scoped>
textarea{
  border-width: 0;
  resize: none;
  background: #fafafa;
  border-radius: 30px;
}
.textarea-container{
  position: relative;
}
.textarea-container textarea{
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
.textarea-container span{
  position: absolute;
  top: 0;
  right: 0;
}
</style>
