<template>
    <div>
      <div class="message-body chat my-1">
          {{msg.txt}}
            <div class="level-right is-size-7 has-text-grey-light">{{msg.time}}</div> 
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
  }
</script>

<style scoped>

hr{
  border-top: 1px solid #b5b5b5;
  margin: 0 1em;
  padding: 0 1em;
}
.chat{
  padding: 0.75em 0.75em;
  border-width: 0 0 0 0;
}
</style>
