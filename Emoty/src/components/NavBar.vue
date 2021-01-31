<template>
    <nav class="navbar is-dark mb-5" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <div class="navbar-item mr-2">

                <img src="../assets/person.png" width="30" height="50">
                <p class="mr-3">Sophie</p>
            </div>
            
        </div>
          <div class="navbar-menu">
                <div class="navbar-start">
                <div class="navbar-item ml-2">
                    <button class="button is-light is-small is-rounded" style="font-weight:bold !important;" 
                    aria-label="After starting session from child side this has to be pressed" data-microtip-position="right" role="tooltip" v-on:click='start_session()'>Start Session</button>

            </div>
                </div>
                </div>
    </nav>
</template>
<script>
export default {
    name: 'NavBar',
    props: {
        msg: String
    },
    methods:{
        start_session() {
            //EventBus.$emit('msg_history_update', msg);
            this.$eventHub.$emit('start_session', 'start');
            console.log('click')
        },
    }
}
</script>
<style scoped>
</style>
