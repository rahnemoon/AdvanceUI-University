import Vue from 'vue';
import Router from 'vue-router';

import Child from './components/Child.vue'
import Therapist from './components/Therapist.vue'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/th/:room_id',
            name: 'Therapist',
            component: Therapist,
        },
        {
            path: '/ch/:room_id',
            name: 'Child',
            component: Child,
        },
        {
            path: '/th',
            name: 'Therapist_without_room',
            component: Therapist,
        },
        {
            path: '/ch',
            name: 'Child_without_room',
            component: Child,
        },
    ],
});
