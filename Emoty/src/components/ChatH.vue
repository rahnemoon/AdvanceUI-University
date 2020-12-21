<template>

  <div class='column is-3 set-height'>
    <div class="has-text-centered has-text-weight-semibold is-size-4 has-text-black mb-4">
    Chat History
    </div>
        <div class="chatHistoryContent has-background-white-bis">

    <ViewChatHistory v-for="h in history" :msg="h" :key="h.id"/>
  </div>
  </div>

</template>

<script>
import ViewChatHistory from './ViewChatHistory.vue'

export default {
  name: 'ChatH',
  components:{
    ViewChatHistory
  },
  
  methods: {
    receive_msg(){
    this.$eventHub.$on('msg_history_update', this.update_nokhod);
    
    },
    update_nokhod(msg){
      console.log(msg);
      this.history.unshift(msg);
      console.log(this.history);
    }
    },
    created() {
    this.receive_msg();
        },

  data(){
    return {
      msg: {},
      history: [],
    }
  }
  }
</script>

<style scoped>
.chatHistoryContent{
  height: 100%;
  width: 100%;
  overflow: auto;
  border-radius: 12px;
}
.set-height {
  height: calc(75vh - 50px);
}

</style>
