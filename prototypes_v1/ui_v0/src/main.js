import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router.js';


Vue.config.productionTip = false
// App is coming from App.vue
new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
