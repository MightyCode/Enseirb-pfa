<template>
    <div class="active-project">
        <span v-if="activeProject === null">Pas de projet actif</span>
        <span v-else>Projet actif: {{ activeProject.id }}</span>
    </div>
    <div class="wrapper">
        <div class="projects-list">
            <h2>Liste des projets existants</h2>
            <div>
                <div class="projects-item" v-for="project in projectList" :key="project.id">
                    {{ project.id }}

                    <div class="item-menu" @click="this.$store.commit('setActiveProject', project);">
                        <div class="icon-wrapper green">
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

        emitter.on('error', (error) => {
            this.error = error;
        });

        emitter.on('fetchProjects', () => {
            this.fetchProjects();
        });
    },
    methods: {
        fetchProjects() {
            axiosInstance.get('/projects')
                .then((response) => {
                    this.projectList = response.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
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
        }
    },
    computed: {
        activeProject() {
            return this.$store.state.activeProject;
        }
    }
}
</script>

<style scoped>
.active-project {
    height: 5%;
    min-height: 2em;
    width: 100%;
    padding: 0 0.5em;

    display: flex;
    align-items: center;
}

.wrapper {
    display: flex;
    flex-direction: row;

    height: 95%;
}

.projects-list {
    width: 20%;

    display: flex;
    flex-direction: column;

    background-color: red;
    border-right: 1px solid #3b3b3b;
}


.projects-list>h2 {
    font-size: 1.2em;
    padding: 0 0.5em;
}

.projects-list>div {
    flex: 1;

    background-color: green;
    overflow-y: auto;
}

.import-wrapper {
    width: 80%;

    display: flex;
    align-items: center;

    flex-direction: column;

    color: black;
    background-color: blue;
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

.active-tab {
    background-color: #4b4b4b;
}

.error-field {
    height: 2em;
    width: 100%;

    display: flex;
    align-items: center;
    justify-content: center;

    background-color: red;
}

.error-field>span {
    background-color: blue;
}

.icon-wrapper {
    width: 1.7em;
    height: 1.7em;
    border-radius: 5px;

    transition-duration: 0.4s;
}

.icon-wrapper:hover {
    cursor: pointer;
    filter: brightness(0.8);
}

.icon-wrapper:first-of-type {
    margin-right: 0.5em;
}

.green {
    background-color: green;
}

.red {
    background-color: red;
}
</style>