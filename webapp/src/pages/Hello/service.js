import client from '@/api';

const service = {
    async getPatients() {
        const resource = 'patients';
        const result = await client.get(resource);
        return result.data;
    },
    async getPatientStudies(patientID) {
        const resource = `patients/${patientID}`;
        const result = await client.get(resource);
        return result.data;
    },
    async getPatientSeries(studyID) {
        const resource = `studies/${studyID}`;
        const result = await client.get(resource);
        return result.data;
    },
    async getPatientInstances(seriesID) {
        const resource = `series/${seriesID}`;
        const result = await client.get(resource);
        return result.data;
    },
    async getImage(instanceID) {
        const resource = `instances/${instanceID}/preview`;
        const result = await client.get(resource);
        console.log(result);

        return result.data;
    },
    async getFrames(instanceID) {
        const resource = `instances/${instanceID}/frames`;
        const result = await client.get(resource);
        return result.data;
    },
};

export default service;