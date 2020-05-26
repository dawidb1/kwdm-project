import Vue from 'vue';
import Router from 'vue-router';
import dashboardRoutes from '@/pages/Dashboard/router'


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
    },
    dashboardRoutes,
  ],
});