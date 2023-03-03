import { createStore } from "vuex";

const store = createStore({
    state() {
        return {
            activeConfig: null,
        }
    },
    mutations: {
        setActiveConfig(state, config) {
            state.activeConfig = config;
        }
    },
    actions: {
        setActiveConfig({ commit }, config) {
            commit('setActiveConfig', config);
        }
    },
});

export default store;
