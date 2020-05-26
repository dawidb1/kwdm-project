import Vue from 'vue';
import Vuex from 'vuex';

import dashboard from './pages/Dashboard/module';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    dashboard,
  },
});