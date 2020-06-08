import dashboardService from './service';

const state = {
    patients: [],
    series: [],
    studies: [],
    instances: [],
    frames: [],
    instanceTags: [],
    segmentizedId: null,
    pendingRequests: 0,
    alreadySegmented: [],
};

const getters = {
    patients: state => state.patients,
    series: state => state.series,
    studies: state => state.studies,
    instances: state => state.instances,
    frames: state => state.frames,
    instanceTags: state => state.instanceTags,
    segmentizedId: state => state.segmentizedId,
    alreadySegmented: state => state.alreadySegmented,
    anyPendingRequests: state => state.pendingRequests > 0,

};

const actions = {
    async getPatients({ commit }) {
        const result = await dashboardService.getPatients();
        commit('setPatients', result);
    },
    async getPatientStudies({ commit }, patientID) {
        const result = await dashboardService.getPatientStudies(patientID);
        commit('setPatientStudies', result);
    },
    async getPatientSeries({ commit }, studyID) {
        const result = await dashboardService.getPatientSeries(studyID);
        commit('setPatientSeries', result);
    },
    async getPatientInstances({ commit }, seriesID) {
        const result = await dashboardService.getPatientInstances(seriesID);
        commit('setInstances', result);
    },
    async getFrames({ commit }, instanceID) {
        const result = await dashboardService.getFrames(instanceID);
        commit('setFrames', result);
    },
    async getInstanceTags({ commit }, instanceID) {
        const result = await dashboardService.getInstanceTags(instanceID);
        commit('setInstanceTags', result);
    },
    async segmentize({ commit }, studyID) {
        const result = await dashboardService.segmentize(studyID);
        commit('setSegmentizedID', result.instanceId);
    },
    async checkIfSegmentized({ commit }, data) {
        const result = await dashboardService.checkIfSegmentized(data);
        commit('setAlreadySegmented', result);
    }
};

const mutations = {
    setPatients(state, result) {
        state.patients = result;
    },
    setPatientStudies(state, result) {
        state.studies = result;
        state.series = [];
        state.instances = [];
        state.image = {};
    },
    setPatientSeries(state, result) {
        state.series = result;
        state.instances = [];
        state.image = {};
    },
    setInstances(state, result) {
        state.instances = result;
    },
    setFrames(state, result) {
        state.frames = result;
    },
    setInstanceTags(state, result) {
        state.instanceTags = result;
    },
    setSegmentizedID(state, result) {
        state.segmentizedId = result;
    },
    setPendingRequest(state) {
        state.pendingRequests++;
      },
      setCompleteRequest(state) {
        state.pendingRequests--;
      },
      setAlreadySegmented(state, data){
          state.alreadySegmented = data;
      },
};

const module = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};

export default module;