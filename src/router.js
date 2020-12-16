import Vue from 'vue';
import Router from 'vue-router';
import Home from "./views/Home.vue";
import Explore from "./views/Explore.vue";
import Help from './views/Help.vue';
import SignUp from './views/SignUp.vue';
import Test from './views/Test.vue';

Vue.use(Router)

export default new Router({
    routes: [
        {
            path:'/Home',
            name: 'Home',
            component: Home
        },
        {
            path:'/Explore',
            name: 'Explore',
            component: Explore
        },
        {
            path:'/SignUp',
            name: 'SignUp',
            component: SignUp
        },
        {
            path:'/Help',
            name: 'Help',
            component: Help
        },
        {
            path:'/Test',
            name: 'Test',
            component: Test
        },
    ],
    mode: 'history',
})