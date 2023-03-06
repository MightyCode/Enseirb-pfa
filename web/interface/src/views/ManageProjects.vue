<template>
    <div class="wrapper">
        <div class="projects-list">
            <h2>Liste des projets existants</h2>
            <div>
                <div class="projects-item" v-for="project in projectsList" :key="project.id"
                    @click="this.$store.commit('setActiveProject', config);"
                    >
                    {{ config.id }}
                </div>
            </div>
        </div>
        <div class="import-wrapper">
            <div class="menu">
                <div 
                    @click="mode = 'CREATE'"
                    :class="{ 'active-tab': mode === 'CREATE'}"
                    >Créer</div>
                <div 
                    @click="mode = 'IMPORT'"
                    :class="{ 'active-tab': mode === 'IMPORT'}"
                    >Importer</div>
            </div>


            <div class="body">
                <div v-if="mode === 'IMPORT'" class="file-selector-wrapper">
                    <FileSelection v-if="!error" accept=".json,.yaml,.yml" />
                    <div class="error-wrapper" v-else>
                        <p>{{ error }}</p>
                        <button @click="error = null">Compris</button>
                    </div>
                </div>
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
            mode: 'IMPORT'
        };
    },
    mounted() {
        axiosInstance.get('/projects')
            .then((response) => {
                this.projectList = response.data;
            })
            .catch((error) => {
                console.error(error);
            });

        emitter.on('fileImported', (file) => {
            const fileReader = new FileReader();

            // POST content of the file to the server as JSON
            fileReader.addEventListener('load', (event) => {
                axiosInstance.post('/projects', JSON.parse(event.target.result))
                    .then((response) => {
                        // If the server returns a 200, the config is valid
                        // We can then set it as the active config
                        this.$store.commit('setActiveProject', response.data);
                    })
                    .catch((error) => {
                        // If the server returns a 400, the config is invalid
                        // If the server returns a 409, the config already exists

                        // We can then display an error message
                        switch (error.response.status) {
                            case 400:
                                this.error = 'Le fichier de projet est invalide';
                                break;
                            case 409:
                                this.error = 'Le fichier de projet existe déjà';
                                break;
                            default:
                                this.error = 'Une erreur est survenue';
                                break;
                        }
                    });
            });

            fileReader.readAsText(file);
        });
    }
}
</script>

<style scoped>
.wrapper {
    display: flex;
    flex-direction: row;

    height: 100%;
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

}

.import-wrapper {
    width: 80%;

    display: flex;
    align-items: center;

    flex-direction: column;

    color: black;
    background-color: blue;
}

.file-selector-wrapper {
    width: 30vw;
    height: 30vw;
}

.error-wrapper {
    width: 100%;
    height: 20%;
    background-color: #3b3b3b;
    color: white;

    display: flex;
    justify-content: center;
    align-items: center;

    flex-direction: column;

    border-radius: 7px;
}

.error-wrapper>p {
    margin: 0 0 1em 0;
    padding: 0;
}

.error-wrapper>button {
    width: 10em;
    height: 2em;

    border-radius: 5px;
    border: 0;
}

.error-wrapper>button:hover {
    cursor: pointer;
}

.error-wrapper>button:focus {
    outline: none;
}

.projects-item {
    width: 100%;
    background-color: #3b3b3b;
    padding: 0.5em 1em;
    transition-duration: 0.4s;
}

.projects-item:hover {
    cursor: pointer;
    background-color: #4b4b4b;
}

.menu {
    width: 100%;
    height: 3em;

    display: flex;
    justify-content: space-around;
    align-items: center;

    border-bottom: #3b3b3b 1px solid;
}

.menu > div {
    width: 50%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    transition-duration: 0.4s;
}

.menu > div:first-of-type {
    border-right: 1px solid #4b4b4b;
}

.menu > div:hover {
    cursor: pointer;
    background-color: #4b4b4b;
}

.body {
    flex: 1;
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
}

.active-tab {
    background-color: #4b4b4b;
}
</style>