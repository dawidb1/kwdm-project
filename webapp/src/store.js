import Vue from 'vue';
import Vuex from 'vuex';

import hello from './pages/Hello/module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    hello,
  },
});