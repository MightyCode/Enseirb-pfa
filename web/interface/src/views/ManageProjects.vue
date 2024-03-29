<template>
    <div class="wrapper">
        <div class="projects-list">
            <h2>Liste des projets existants</h2>
            <div>
                <div class="projects-item" v-for="project in projectList" :key="project.id">
                    {{ project.id }}

                    <div class="item-menu">
                        <div class="icon-wrapper" :class="getActiveProjectButtonClass(project)" @click="onSetActiveProjectButtonClick(project)">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                            </svg>
                        </div>

                        <div class="icon-wrapper red" @click="deleteProject(project)">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </div>
                    </div>

                </div>
            </div>
        </div>
        <div class="import-wrapper">
            <div class="menu">
                <router-link to="/projects/" class="link">Créer</router-link>
                <router-link to="/projects/import" class="link">Importer</router-link>
            </div>


            <div class="body">
                <div class="error-field">
                    <span>{{ error }}</span>
                </div>
                <router-view />
            </div>
        </div>
    </div>
</template>

<script>
import FileSelection from '../components/FileSelection.vue'
import emitter from '../emitter';
import axiosInstance from '../axiosInstance';

export default {
    name: 'ManageProjects',
    components: {
        FileSelection
    },
    data() {
        return {
            error: '',
            projectList: [],
            createdProject: null
        };
    },
    mounted() {
        this.fetchProjects();

        // Display error message if there is one
        emitter.on('error', (error) => {
            this.error = error;
        });

        // Listen when children wants to refresh the project list
        emitter.on('fetchProjects', () => {
            this.fetchProjects();
        });
    },
    methods: {
        /**
         * Fetches projects from the backend
         */
        fetchProjects() {
            axiosInstance.get('/projects')
                .then((response) => {
                    this.projectList = response.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },

        /**
         * Deletes a project from the backend
         * @param {Object} project The project to delete 
         */
        deleteProject(project) {
            axiosInstance.delete(`/projects/${project.id}`)
                .then(() => {
                    this.fetchProjects();

                    // Set active project to null if it is the one we deleted
                    if (this.activeProject && this.activeProject.id === project.id) {
                        this.$store.commit('setActiveProject', null);
                    }
                })
                .catch((error) => {
                    console.error(error);
                });
        },

        /**
         * Sets the active project when the user clicks on a project button
         * @param {Object} project The project to set as active
         */
        onSetActiveProjectButtonClick(project) {
            if ((!this.activeConfig) || this.activeConfig.id !== project.config) {
                return;
            }

            this.$store.commit('setActiveProject', project);
        },

        /**
         * Gets the CSS class for the active project button
         * @param {Object} project The project to get the class for
         */
        getActiveProjectButtonClass(project) {
            if (this.activeConfig && this.activeConfig.id === project.config) {
                return 'green';
            }

            return 'green-disabled';
        }
    },
    computed: {
        activeProject() {
            return this.$store.state.activeProject;
        },
        activeConfig() {
            return this.$store.state.activeConfig;
        }
    }
}
</script>

<style scoped>
.wrapper {
    display: flex;
    flex-direction: row;

    height: 100%;
    color: black;   
}

.projects-list {
    width: 20%;

    display: flex;
    flex-direction: column;

    border-right: 1px solid #3b3b3b;
    background-color: #5b5b5b;
}


.projects-list>h2 {
    font-size: 1.2em;
    padding: 1em 0.5em;
    margin: 0;
    border-bottom: 1px solid #3b3b3b;
}

.projects-list>div {
    flex: 1;

    overflow-y: auto;
}

.import-wrapper {
    width: 80%;

    display: flex;
    align-items: center;

    flex-direction: column;

    color: black;
}


.projects-item {
    width: 100%;
    background-color: #3b3b3b;
    padding: 0.5em 1em;
    transition-duration: 0.4s;

    display: flex;
    justify-content: space-between;
}

.projects-item>div {
    display: flex;
}

.menu {
    width: 100%;
    height: 3em;

    display: flex;
    justify-content: space-around;
    align-items: center;

    border-bottom: #3b3b3b 1px solid;
    background-color: #5b5b5b;
}

.menu>.link {
    width: 50%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    transition-duration: 0.4s;
}

.link {
    color: black;
    text-decoration: none;
}

.link:visited {
    color: black;
    text-decoration: none;
}

.menu>.link:first-of-type {
    border-right: 1px solid #4b4b4b;
}

.menu>.link:hover {
    cursor: pointer;
    background-color: #4b4b4b;
}

.body {
    flex: 1;
    width: 100%;

    display: flex;
    align-items: center;

    flex-direction: column;
}

.error-field {
    height: 2em;
    width: 100%;

    display: flex;
    align-items: center;
    justify-content: center;
}

.error-field>span {
    color: #aa0000;
}

.icon-wrapper {
    width: 1.7em;
    height: 1.7em;
    border-radius: 5px;

    transition-duration: 0.4s;
    color: white;
}

.red:hover {
    cursor: pointer;
    filter: brightness(0.8);
}

.green:hover {
    cursor: pointer;
    filter: brightness(0.8);
}

.icon-wrapper:first-of-type {
    margin-right: 0.5em;
}

.green {
    background-color: green;
}

.green-disabled {
    background-color: #226600;
}

.red {
    background-color: red;
}
</style>