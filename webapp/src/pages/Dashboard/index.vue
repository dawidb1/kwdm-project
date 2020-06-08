<template>
  <div style="background: #d6f5d6; height: 100%;">
    <div class="header">Internetowa stacja wspomagania segmentacji obrazów medycznych</div>
    <div class="d-flex" style="padding: 40px;">
      <div class="left-container">
        <div class="action-button-container">
          <p>
            <b>Pacjenci:</b>
          </p>
          <v-btn
            class="action-button"
            outlined
            rounded
            v-for="patient in patients"
            :key="patient.ID"
            @click="getStudies(patient.ID)"
          >{{patient.patientName}}</v-btn>
          <div v-if="studiesClicked" class="action-button-container">
            <p>
              <b>Badania:</b>
            </p>
            <v-btn
              class="action-button"
              outlined
              rounded
              v-for="(study, index) in studies.Studies"
              :key="study"
              @click="getSeries(study)"
            >Badanie {{index + 1}}</v-btn>
          </div>
          <div v-if="seriesClicked" class="action-button-container">
            <p>
              <b>Serie:</b>
            </p>

            <v-btn
              class="action-button"
              outlined
              rounded
              v-for="(item, index) in series.Series"
              :key="item"
              @click="getInstances(item);"
            >Seria {{index + 1}}</v-btn>
          </div>
          <div v-if="instancesClicked" class="action-button-container">
            <p>
              <b>Obrazy:</b>
            </p>
            <v-btn
              class="action-button"
              outlined
              rounded
              v-for="(item, index) in instances.Instances"
              :key="item"
              @click="getFramesForInstance(item)"
            >Obraz {{index + 1}}</v-btn>
          </div>
        </div>
      </div>
      <div class="right-container" v-if="showImageClicked">
        <div class="image-container" v-if="selectedFrame !== null">
          <div class="center-img">
            <img class="image" :src="imageData" />
          </div>
          <label>Wybrany przekrój: {{selectedFrame}}</label>
          <v-slider
            v-model="selectedFrame"
            class="align-center"
            :max="frames.length-1"
            :min="0"
            hide-details
          ></v-slider>
            <v-btn
              outlined
              rounded
              style="background: #F9F9F9;"
              v-for="item in instances.Instances"
              :key="item"
              @click="predict(item)"
              :disabled="!segmentButtonActive"
            >Segmentuj obraz</v-btn>

        </div>
        <div class="image-container" v-if="selectedFrame2 !== null && !segmentButtonActive && !isPrediction" >
          <v-tooltip right>
            <template v-slot:activator="{ on }">
              <div class="center-img">
                <img class="image-segmentation" v-on="on" :src="imageData2" />
              </div>
            </template>
            <span>Wysegmentowany obraz</span>
          </v-tooltip>

          <label v-if="segmentizedId !== null">Wybrany przekrój: {{selectedFrame2}}</label>
          <v-slider
            v-if="segmentizedId !== null"
            v-model="selectedFrame2"
            class="align-center"
            :max="frames.length-1"
            :min="0"
            hide-details
          ></v-slider>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
  name: "Dashboard",
  data() {
    return {
      imageData: null,
      imageData2: null,
      selectedFrame: null,
      selectedFrame2: null,
      selectedInstanceId: null,
      studiesClicked: false,
      seriesClicked: false,
      instancesClicked: false,
      segmentDisable: false,
      segmentButtonActive: true,
      showImageClicked: false,
      isPrediction: true,
    };
  },
  watch: {
    selectedFrame() {
      if (this.selectedInstanceId !== null) {
        this.showImage(this.selectedInstanceId);
        this.selectedFrame2 = this.selectedFrame;
      }
    },
    selectedFrame2() {
      if (this.segmentizedId !== null) {
        this.showSegmentedImage();
        this.selectedFrame = this.selectedFrame2;
      }
    }
  },
  methods: {
    ...mapActions("dashboard", [
      "getImage",
      "getPatients",
      "getPatientStudies",
      "getPatientSeries",
      "getPatientInstances",
      "getFrames",
      "getInstanceTags",
      "segmentize",
      "checkIfSegmentized"
    ]),
    ...mapMutations("dashboard", ["setSegmentizedID"]),
    getStudies(patientID) {
      this.getPatientStudies(patientID);
      this.segmentButtonActive = true;
      this.studiesClicked = true;
      this.seriesClicked = false;
      this.instancesClicked = false;
      this.showImageClicked = false;
      this.isPrediction = false;

    },
    getSeries(studyID) {
      this.getPatientSeries(studyID);
      this.seriesClicked = true;
      this.showImageClicked = false;
      this.instancesClicked = false;
      this.isPrediction = false;


    },
    getInstances(seriesID) {
      this.getPatientInstances(seriesID);
      this.instancesClicked = true;
      this.showImageClicked = false;
    },
    async getFramesForInstance(instanceID) {
      this.getFrames(instanceID);
      this.selectedInstanceId = instanceID;
      await this.getInstanceTags(instanceID);
      if (this.instanceTags.Modality === "PRED") {
        this.isPrediction = true;
      }
      await this.checkIfSegmentized(this.instanceTags.StudyID);

    
     if (this.alreadySegmented.length > 0) {
        this.segmentButtonActive = false;
        await this.setSegmentizedID(this.alreadySegmented[0]);
        this.selectedFrame2 = 1;
        this.showSegmentedImage();
      } else {
        this.segmentButtonActive = true;
      }
      this.selectedFrame = 1;
      this.showImageClicked = true;
    },
    showImage(instanceID) {
      // todo pin to api service with headers authorization
      this.selectedFrame === null ? 0 : this.selectedFrame;
      fetch(
        `/orthanc/instances/${instanceID}/frames/${this.selectedFrame}/preview`
      )
        .then(function(data) {
          return data.blob();
        })
        .then(
          function(img) {
            var dd = URL.createObjectURL(img);
            this.imageData = dd;
          }.bind(this)
        );
      this.segmentDisable = false;
    },
    showSegmentedImage() {
      // todo pin to api service with headers authorization
      fetch(
        `/orthanc/instances/${this.segmentizedId}/frames/${this.selectedFrame2}/preview`
      )
        .then(function(data) {
          return data.blob();
        })
        .then(
          function(img) {
            var dd = URL.createObjectURL(img);
            this.imageData2 = dd;
          }.bind(this)
        );
    },
    async predict(instanceID) {
      await this.getInstanceTags(instanceID);  
      await this.segmentize(this.instanceTags.StudyID);
      
      this.selectedFrame2 = 1;
      this.showSegmentedImage();
      this.segmentButtonActive = false;
    }
  },
  created() {
    this.getPatients();
  },
  computed: {
    ...mapGetters("dashboard", [
      "patients",
      "studies",
      "series",
      "instances",
      "frames",
      "instanceTags",
      "segmentizedId",
      "alreadySegmented"
    ]),
    segmentationDisable() {
      return this.segmentDisable;
    }
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

.left-container {
  height: 100%;
  width: 50%;
}

.right-container {
  height: 100%;
  width: 50%;
}

.image {
  width: 350px;
  height: 350px;
  margin-bottom: 10px;
}
.image-segmentation {
  width: 350px;
  height: 350px;
  margin-bottom: 20px;
  transform: rotate(180deg);
}
.center-img {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.image-container {
  display: flex;
  flex-direction: column;
  margin-left: 20px;
  margin-bottom: 20px;
}

.action-button {
  margin: 5px;
  width: 500px;
  background: #f9f9f9;
}

.action-button-container {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.header {
  height: 50px;
  width: 100%;
  background: #d6f5d6;
  text-align: center;
  padding-top: 10px;
  border-bottom: 1px solid;
}
</style>
