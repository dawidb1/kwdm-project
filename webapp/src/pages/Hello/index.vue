<template>
  <div style="padding: 40px;">
    <p>
      Pacjenci:
      <v-btn
        v-for="patient in patients"
        :key="patient"
        @click="getStudies(patient)"
      >Pacjent o id: {{patient}}</v-btn>
    </p>
    <p>
      Badania:
      <v-btn
        v-for="study in studies.Studies"
        :key="study"
        @click="getSeries(study)"
      >Badanie: {{study}}</v-btn>
    </p>
    <p>
      Serie:
      <v-btn v-for="item in series.Series" :key="item" @click="getInstances(item)">Seria: {{item}}</v-btn>
    </p>
    <p>
      Obrazy:
      <v-btn
        v-for="item in instances.Instances"
        :key="item"
        @click="showImage(item)"
      >Obraz: {{item}}</v-btn>
    </p>
    <img :src="image" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "HelloWorld",
  data() {
    return {
      imageData: ""
    };
  },
  methods: {
    ...mapActions("hello", [
      "getImage",
      "getPatients",
      "getPatientStudies",
      "getPatientSeries",
      "getPatientInstances",
      "getImage"
    ]),
    getStudies(patientID) {
      this.getPatientStudies(patientID);
    },
    getSeries(studyID) {
      this.getPatientSeries(studyID);
    },
    getInstances(seriesID) {
      this.getPatientInstances(seriesID);
    },
    showImage(instanceID) {
      this.getImage(instanceID);
    }
  },
  created() {
    this.getPatients();
  },
  computed: {
    ...mapGetters("hello", [
      "patients",
      "studies",
      "series",
      "instances",
      "image"
    ])
  }
};
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
