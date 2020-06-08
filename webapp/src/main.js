import Vue from 'vue'
import App from './App.vue'
import store from './store';
import vuetify from './plugins/vuetify';
import router from './router';
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';
import Loader from './components/Loader'

Vue.config.productionTip = false
Vue.use(Loading);
Vue.component('Loader', Loader);
new Vue({
  router,
  vuetify,
  store,
  render: h => h(App),
}).$mount('#app')
