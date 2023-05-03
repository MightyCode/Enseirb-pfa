<template>
    <div class="wrapper">
        <div class="configs-list">
            <h2>Liste des configurations existantes</h2>
            <div>
                <div class="configs-item" v-for="config in configList" :key="config.id">
                    {{ config.id }}

                    <div class="item-menu">
                        <div class="icon-wrapper green" @click="onSetActiveConfigButtonClick(config)">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                            </svg>
                        </div>

                        <div class="icon-wrapper red" @click="deleteConfig(config)">
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
                <router-link to="/configs/" class="link">Créer</router-link>
                <router-link to="/configs/import" class="link">Importer</router-link>
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
    name: 'ManageConfigs',
    components: {
        FileSelection
    },
    data() {
        return {
            error: '',
            configList: [],
            createdConfig: null
        };
    },
    mounted() {
        this.fetchConfigs();

        emitter.on('error', (error) => {
            this.error = error;
        });

        emitter.on('fetchConfigs', () => {
            this.fetchConfigs();
        });
    },
    methods: {
        fetchConfigs() {
            axiosInstance.get('/configs')
                .then((response) => {
                    this.configList = response.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        deleteConfig(config) {
            axiosInstance.delete(`/configs/${config.id}`)
                .then(() => {
                    this.fetchConfigs();

                    // Set active config to null if it is the one we deleted
                    if (this.activeConfig && this.activeConfig.id === config.id) {
                        this.$store.commit('setActiveConfig', null);
                    }
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        onSetActiveConfigButtonClick(config) {
            this.$store.commit('setActiveConfig', config);
            
            // Reset active project
            this.$store.commit('setActiveProject', null);
        }
    },
    computed: {
        activeConfig() {
            return this.$store.state.activeConfig;
        }
    }
}
</script>

<style scoped>
.active-config {
    height: 5%;
    min-height: 2em;
    width: 100%;
    padding: 0 0.5em;

    display: flex;
    align-items: center;

    color: black;
}

.wrapper {
    display: flex;
    flex-direction: row;

    height: 100%;
    color: black;   
}

.configs-list {
    width: 20%;

    display: flex;
    flex-direction: column;

    border-right: 1px solid #3b3b3b;
    background-color: #5b5b5b;
}


.configs-list>h2 {
    font-size: 1.2em;
    padding: 1em 0.5em;
    margin: 0;
    border-bottom: 1px solid #3b3b3b;
}

.configs-list>div {
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


.configs-item {
    width: 100%;
    background-color: #3b3b3b;
    padding: 0.5em 1em;
    transition-duration: 0.4s;

    display: flex;
    justify-content: space-between;
}

.configs-item>div {
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