<template>
      <div>
            <div class="dropdown-item popup-item-width">
                  <button @click="selectedQuickReaction(reaction)" :id="reaction.id">
                  <img :src="set_img_directory(reaction.emoji)">
                  <span>{{reaction.key}}</span>
                  </button>
            </div><hr>
      </div>


</template>

<script>
export default {
  name: 'QReactionView',
  props: {
    reaction: Object
  },
  
  methods:{
    set_img_directory(assetName){      
      return  require('../assets/mini-emoji/'+assetName);
    },
    selectedQuickReaction(reaction){
      this.$emit("selectedReaction", reaction);
    }
  }
  }
</script>

<style scoped>
hr{
  margin: 0 0 0 0px;
  margin-left: 20px;
  margin-right: 20px;
}
.popup-item-width{
  min-width: 20rem;
}
img {
  width: 20px;
  height: 20px;
  margin-right: 0.5em;
}
button {
  width: 100%;
  height: 100%;
  border: 0px;
  text-align: left;
  background: white;
  outline: 0;
}
button:hover {
  box-shadow: 0 0 4pt 1pt rgba(30,136,229 ,0.5);
  background: rgba(30,136,229 ,0.5);
  border-radius: 10px;
}
button:active {
  box-shadow: 0 0 4pt 1pt rgba(30,136,229 ,0.8);
  background: rgba(30,136,229 ,0.8);
}
</style>
