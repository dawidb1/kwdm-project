import axios from 'axios';

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
});

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
};

export default client;