import client from '@/api';

const service = {
  async getFile() {
    const resource = 'www';
    const result = await client.get(resource);
    return result.data;
  },
};

export default service;
