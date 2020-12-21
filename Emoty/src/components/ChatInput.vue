<template>
  <div class='column is-9'>
      <div class="control textarea-container has-fixed-size">
        <textarea class="textarea" placeholder="Text input" rows="1" v-model="input_txt" @keyup.enter="on_submit()"></textarea>
        <span class="mr-5 mt-2" v-on:click="on_submit()">
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
    msg: String,
  },
  methods: {
    send_message(msg){
      const url = "http://localhost:5000/text-input";
      axios.post(url, msg)
      .catch((error) => {console.log(error);});
    },
    on_submit(){
      this.msg_id++;
      var today = new Date();
      var time = today.getHours() + ":" + today.getMinutes();
      const msg = {
      txt: this.input_txt,
      id:this.msg_id,
      time: time,
      };
      this.update_history(msg);
      this.send_message(msg);
      this.input_txt = "";
    },
    update_history(msg){
      //EventBus.$emit('msg_history_update', msg);
      this.$eventHub.$emit('msg_history_update', msg);
    } 
  },
  data: function(){
    return{
      input_txt: null,
      msg_id: 0,
      
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
