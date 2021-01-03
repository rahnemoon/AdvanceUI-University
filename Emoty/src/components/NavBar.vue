<template>

<nav class="navbar is-dark mb-5" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <div class="navbar-item mr-2">
      <img src="../assets/person.png" width="30" height="50" style="float: right">
      <p class="mr-3">Sophie</p>
    </div>
  </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    msg: String
  }
}
</script>
<style scoped>
</style>
