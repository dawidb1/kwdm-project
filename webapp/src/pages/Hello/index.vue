<template>
  <div class="hello" style="padding: 40px;">
    <h1>{{ msg }}</h1>
    <p>
      Przykładowe sprawdzenie requesta:
      <v-btn @click="getFileFromServer()">Strzelaj</v-btn>
    </p>

  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

    methods: {
    ...mapActions('hello', [
      'getFile',
    ]),
    getFileFromServer() {
      this.getFile();
    },
  },
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
