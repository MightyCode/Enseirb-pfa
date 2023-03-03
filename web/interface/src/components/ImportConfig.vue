<template>
    <div class="wrapper">
        <h2>Importer un fichier de configuration</h2>
        <div class="file-selector-wrapper">
            <FileSelection accept=".json,.yaml,.yml" />
        </div>
    </div>
</template>

<script>
import FileSelection from './FileSelection.vue'
import emitter from '../emitter';
import axiosInstance from '../axiosInstance';

export default {
    name: 'ImportConfig',
    components: {
        FileSelection
    },
    mounted() {
        emitter.on('fileImported', (file) => {
            const fileReader = new FileReader();

            // POST content of the file to the server as JSON
            fileReader.addEventListener('load', (event) => {                
                axiosInstance.post('/configs', JSON.parse(event.target.result))
                    .then((response) => {
                        // If the server returns a 200, the config is valid
                        // We can then set it as the active config
                        this.$store.commit('setActiveConfig', response.data);
                    })
                    .catch((error) => {
                        // If the server returns a 400, the config is invalid
                        // We can then display an error message
                        console.log(error);
                    });
            });

            fileReader.readAsText(file);
        });
    }
}
</script>

<style scoped>
.wrapper {
    width: 100%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    flex-direction: column;

    color: black;
}

.wrapper>.file-selector-wrapper {
    width: 30vw;
    height: 30vw;
}
</style>