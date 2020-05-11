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
      <v-btn
        v-for="item in series.Series"
        :key="item"
        @click="getInstances(item);"
      >Seria: {{item}}</v-btn>
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

      <p>
      Segmentacja:
      <v-btn
        v-for="item in instances.Instances"
        :key="item"
        @click="predict(item)"
      >Segmentacja: {{item}}</v-btn>
    </p>

     <img :src="imageData2" />
    <label v-if="selectedFrame2 !== null">Wybrany przekrój: {{selectedFrame2}}</label>
    <v-slider
      v-if="selectedFrame2 !== null"
      v-model="selectedFrame2"
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
      imageData: null,
      imageData2: null,
      selectedFrame: null,
      selectedFrame2: null,
      selectedInstanceId: null
    };
  },
  watch: {
    selectedFrame() {
      if (this.selectedInstanceId !== null) {
        this.showImage(this.selectedInstanceId);
      }
    },
    selectedFrame2() {
      if (this.segmentizedId !== null) {
        this.showSegmentedImage();
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
      "getFrames",
      "getInstanceTags",
      "segmentize"
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
      // todo pin to api service with headers authorization
      fetch(
        `/orthanc/instances/${instanceID}/frames/${this.selectedFrame}/preview`
      )
        .then(function(data) {
          return data.blob();
        })
        .then(function(img) {
          var dd = URL.createObjectURL(img);
          this.imageData = dd;
        }.bind(this));
    },
     showSegmentedImage() {
      // todo pin to api service with headers authorization
      fetch(
        `/orthanc/instances/${this.segmentizedId}/frames/${this.selectedFrame2}/preview`
      )
        .then(function(data) {
          return data.blob();
        })
        .then(function(img) {
          var dd = URL.createObjectURL(img);
          this.imageData2 = dd;
        }.bind(this));
    },
    async predict(instanceID) {
      
      await this.getInstanceTags(instanceID);
      await this.segmentize(this.instanceTags.StudyID);
      this.selectedFrame2 = 0;
      this.showSegmentedImage();
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
      "frames",
      "instanceTags",
      "segmentizedId"
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
