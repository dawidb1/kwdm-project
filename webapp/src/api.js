import axios from "axios";
import store from '@/store';

const api = axios.create({
  baseURL: "/orthanc/",
  auth: {
    username: "demo",
    password: "demo",
  },
});

const segmentationApi = axios.create({
  baseURL: "",
  auth: {
    username: "demo",
    password: "demo",
  },
});
api.interceptors.request.use(
  (config) => {
    if (!config.url.includes('SaveUserSettings')) {
      store.commit('dashboard/setPendingRequest');
    }
    return config;
  },

  error => Promise.reject(error)
);
api.interceptors.response.use(
  (response) => {
    if (!response.config.url.includes('SaveUserSettings')) {
      store.commit('dashboard/setCompleteRequest');
    }
    return response;
  },
  (error) => {
    store.commit('dashboard/setCompleteRequest');
    return Promise.reject(error);
  }
);

const client = {
  async get(resource, params) {
    const config = {
      params,
    };
    const result = await api.get(resource, config);
    return result;
  },
  async post(resource, data, params) {
    const config = {
      params,
    };
    const result = await api.post(resource, data, config);
    return result;
  },
  async delete(resource, params = true) {
    const config = {
      params,
    };
    const result = await api.delete(resource, config);
    return result;
  },

  async getSegmentation(resource, params) {
    const config = {
      params,
    };
    const result = await segmentationApi.get(resource, config);
    return result;
  },
};

export default client;
