<template>
    <div class="file-selector-wrapper">
        <FileSelection accept=".json,.yaml,.yml" />
    </div>
</template>

<script>
import FileSelection from '../../components/FileSelection.vue';
import emitter from '../../emitter';
import axiosInstance from '../../axiosInstance';

export default {
    name: "ImportProject",
    components: {
        FileSelection
    },
    mounted() {
        emitter.on('fileImported', (file) => {
            const fileReader = new FileReader();

            // POST content of the file to the server as JSON
            fileReader.addEventListener('load', (event) => {
                axiosInstance.post('/projects', JSON.parse(event.target.result))
                    .then((response) => {
                        // If the server returns a 200, the config is valid
                        // We can then set it as the active config
                        this.$store.commit('setActiveProject', response.data);

                        // Fetch the list of projects again
                        emitter.emit('fetchProjects');
                    })
                    .catch((error) => {
                        // If the server returns a 400, the config is invalid
                        // If the server returns a 409, the config already exists

                        // We can then display an error message
                        emitter.emit('error', error.response.data.error)
                    });
            });

            fileReader.readAsText(file);
        });
    }
}
</script>

<style scoped>
.file-selector-wrapper {
    width: 30vw;
    height: 30vw;
}
</style>