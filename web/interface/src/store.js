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
            if (config) {
                console.log('[PROJECT] Setting active config to', config.id)
            } else {
                console.log('[PROJECT] Setting active config to null')
            }
            state.activeConfig = config;
        },
        setActiveProject(state, project) {
            if (project) {
                console.log('[PROJECT] Setting active project to', project.id)
            } else {
                console.log('[PROJECT] Setting active project to null')
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
});

export default store;
