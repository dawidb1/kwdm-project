import helloService from './service';

const state = {
    patients: [],
    series: [],
    studies: [],
    instances: [],
    frames: [],
    instanceTags: [],
    segmentizedId: null,
};

const getters = {
    patients: state => state.patients,
    series: state => state.series,
    studies: state => state.studies,
    instances: state => state.instances,
    frames: state => state.frames,
    instanceTags: state => state.instanceTags,
    segmentizedId: state => state.segmentizedId
};

const actions = {
    async getPatients({ commit }) {
        const result = await helloService.getPatients();
        commit('setPatients', result);
    },
    async getPatientStudies({ commit }, patientID) {
        const result = await helloService.getPatientStudies(patientID);
        commit('setPatientStudies', result);
    },
    async getPatientSeries({ commit }, studyID) {
        const result = await helloService.getPatientSeries(studyID);
        commit('setPatientSeries', result);
    },
    async getPatientInstances({ commit }, seriesID) {
        const result = await helloService.getPatientInstances(seriesID);
        commit('setInstances', result);
    },
    async getFrames({ commit }, instanceID) {
        const result = await helloService.getFrames(instanceID);
        commit('setFrames', result);
    },
    async getInstanceTags({ commit }, instanceID) {
        const result = await helloService.getInstanceTags(instanceID);
        commit('setInstanceTags', result);
    },
    async segmentize({ commit }, studyID) {
        const result = await helloService.segmentize(studyID);
        commit('setSegmentizedID', result.instanceId);
    },
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
};

const module = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};

export default module;