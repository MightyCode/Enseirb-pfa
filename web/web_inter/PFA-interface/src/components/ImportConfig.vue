<template>
    <div class="wrapper">
        <h2>Importer un fichier de configuration</h2>
        <div class="file-selector-wrapper">
            <FileSelection accept=".json,.yaml,.yml"/>
        </div>
    </div>
</template>

<script>
import FileSelection from './FileSelection.vue'
import emitter from '../emitter';

export default {
    name: 'ImportConfig',
    components: {
        FileSelection
    },
    mounted() {
        emitter.on('fileImported', (file) => {
            this.$store.commit('setActiveConfig', file);
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