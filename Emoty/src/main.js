import 'bulma/css/bulma.css';
import Vue from 'vue'
import App from './App.vue'
import router from './router';
import microtip from 'microtip/microtip.css'


Vue.config.productionTip = false
Vue.prototype.$eventHub = new Vue();

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
