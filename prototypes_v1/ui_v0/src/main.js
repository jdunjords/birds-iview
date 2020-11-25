import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router';
import Explore from './components/Explore';
import Home from './components/Home';
import Demo from './components/Demo';
import Signup from './components/Signup';
// import Axios from 'axios';


Vue.config.productionTip = false
Vue.use(VueRouter);

const routes = [
  { path: '/explore', component: Explore },
  { path: '/home', component: Home },
  { path: '/', component: Home },
  { path: '/demo', component: Demo },
  { path: '/signup', component: Signup },
];
const router = new VueRouter({
  routes,
  mode: 'history'
})
new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

