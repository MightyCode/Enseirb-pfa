import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

const store = createStore({
    state() {
        return {
            activeConfig: null,
            activeProject: null,
        }
    },
    mutations: {
        setActiveConfig(state, config) {
            if (config) {
                console.info('[store.js:PROJECT] Setting active config to', config.id)
            } else {
                console.info('[store.js:PROJECT] Setting active config to null')
            }
            state.activeConfig = config;
        },
        setActiveProject(state, project) {
            if (project) {
                console.info('[store.js:PROJECT] Setting active project to', project.id)
            } else {
                console.info('[store.js:PROJECT] Setting active project to null')
            }
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
    plugins: [createPersistedState()]
});

export default store;
