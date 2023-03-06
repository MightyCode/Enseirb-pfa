import { createStore } from "vuex";

const store = createStore({
    state() {
        return {
            activeConfig: null,
            activeProject: null,
        }
    },
    mutations: {
        setActiveConfig(state, config) {
            console.log('[CONFIG] Setting active config to', config.id)
            state.activeConfig = config;
        },
        setActiveProject(state, project) {
            console.log('[PROJECT] Setting active project to', project.id)
            state.activeProject = project;
        }
    },
    actions: {
        setActiveConfig({ commit }, config) {
            commit('setActiveConfig', config);
        },
        setActiveProject({ commit }, project) {
            commit('setActiveProject', project);
        }
    },
});

export default store;
