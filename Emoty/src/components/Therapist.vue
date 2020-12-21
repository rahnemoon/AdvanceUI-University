<template>
  <div>
    <NavBar dir="rtl"/>
    <div class='columns is-2 mx-2'>
      <Stream/>
      <ChatH/>
    </div>

    <div class='columns is-2 mx-2'>
      <ChatInput/>
      <QuickR/>
    </div>
    </div>
</template>

<script>
import Stream from './Stream.vue'
import ChatH from './ChatH.vue'
import QuickR from './QuickR.vue'
import ChatInput from './ChatInput.vue'
import NavBar from './NavBar.vue'


export default {
  name: 'Therapist',
  components: {
    Stream,
    ChatH,
    QuickR,
    ChatInput,
    NavBar
    
  }
}
</script>

<style>

</style>
