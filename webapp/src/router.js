import Vue from 'vue';
import Router from 'vue-router';
import helloRoutes from '@/pages/Hello/router'


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/hello',
    },
    helloRoutes,
  ],
});