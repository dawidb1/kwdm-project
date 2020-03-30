import helloService from './service';

const state = {
    image: {},
};

const getters = {
};

const actions = {
  async getImage({ commit }) {
   const result = await helloService.getImage();
    commit('setImage', result);
  },
};

const mutations = {
    setImage(state, result) {
    state.image = result;
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
