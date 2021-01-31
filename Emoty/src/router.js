import Vue from 'vue';
import Router from 'vue-router';

import Child from './components/Child.vue'
import Therapist from './components/Therapist.vue'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/th',
            name: 'Therapist',
            component: Therapist,
        },

        {
            path: '/ch',
            name: 'Child',
            component: Child,
        },
    ],
});
