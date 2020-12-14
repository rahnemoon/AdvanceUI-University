<template>

  <div class='column is-3'>
    <div class="has-text-centered has-text-weight-semibold is-size-4 has-text-black mb-5">
    Chat History
    </div>
    <div class="chatHistoryContent has-background-white-bis">
      <div class="message-body my-1 chat">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            <div class="level-right is-size-7 has-text-grey-light">10:2</div> 
        </div>
        <hr>
      <div class="message-body my-1 chat">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            <div class="level-right is-size-7 has-text-grey-light">10:2</div> 
        </div>
        <hr>
      <div class="message-body my-1 chat">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            <div class="level-right is-size-7 has-text-grey-light">10:2</div> 
        </div>
        <hr>
      <div class="message-body my-1 chat">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            <div class="level-right is-size-7 has-text-grey-light">10:2</div> 
        </div>
        <hr>
      <div class="message-body my-1 chat">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            <div class="level-right is-size-7 has-text-grey-light">10:2</div> 
        </div>
        <hr>
      <div class="message-body my-1 chat">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            <div class="level-right is-size-7 has-text-grey-light">10:2</div> 
        </div>
        
    </div>
  </div>

</template>

<script>
export default {
  name: 'ChatH',
  props: {
    msg: String
  }
}
</script>

<style scoped>
.chatHistoryContent{
  max-height: 25em;
  overflow: auto;
  border-radius: 12px;
}
.chat{
  padding: 0.75em 0.75em;
  border-width: 0 0 0 0;
}
hr{
  border-top: 1px solid #b5b5b5;
  margin: 0 1em;
  padding: 0 1em;
}
</style>
