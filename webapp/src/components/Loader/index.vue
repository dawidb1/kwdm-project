<template>
  <loading :active.sync="anyPendingRequests" :can-cancel="true" :z-index="9999"></loading>
</template>

<script>
import { mapGetters } from 'vuex';
import Loading from 'vue-loading-overlay';

export default {
  name: "Loader",
  components: {
    Loading,
  },
  computed: {
    ...mapGetters('dashboard', ['anyPendingRequests']),
  },
};
</script>
