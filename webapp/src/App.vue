<template>
  <v-app>
    <v-content>
      <Loader />
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Loader from '@/components/Loader';

export default {
  name: 'App',

  data: () => ({
      components: {
    Loader,
      }
  }),
};
</script>
