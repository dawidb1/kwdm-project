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
        @click="getFramesForInstance(item)"
      >Obraz: {{item}}</v-btn>
    </p>
    <img :src="imageData" />
    <label v-if="selectedFrame !== null">Wybrany przekrój: {{selectedFrame}}</label>
    <v-slider
      v-if="selectedFrame !== null"
      v-model="selectedFrame"
      class="align-center"
      :max="frames.length-1"
      :min="0"
      hide-details
    ></v-slider>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "HelloWorld",
  data() {
    return {
      imageData: "",
      selectedFrame: null,
      selectedInstanceId: null
    };
  },
  watch: {
    selectedFrame() {
      if (this.selectedInstanceId !== null) {
        this.showImage(this.selectedInstanceId);
      }
    }
  },
  methods: {
    ...mapActions("hello", [
      "getImage",
      "getPatients",
      "getPatientStudies",
      "getPatientSeries",
      "getPatientInstances",
      "getFrames"
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
    getFramesForInstance(instanceID) {
      this.getFrames(instanceID);
      this.selectedInstanceId = instanceID;
      this.selectedFrame = 0;
    },
    showImage(instanceID) {
      var that = this;
      // todo pin to api service with headers authorization
      fetch(
        `/orthanc/instances/${instanceID}/frames/${this.selectedFrame}/preview`
      )
        .then(function(data) {
          return data.blob();
        })
        .then(function(img) {
          var dd = URL.createObjectURL(img);
          that.imageData = dd;
        });
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
      "frames"
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
