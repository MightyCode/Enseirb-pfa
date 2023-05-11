<template>
    <div class="wrapper">
        <div class="column">
            <div class="field-wrapper">
                <label for="name">Nom</label>
                <input type="text" id="name" v-model="name">
            </div>

            <div class="field-wrapper">
                <label for="name">Nombre de lumières</label>
                <input type="number" id="name" v-model="nbLights">
            </div>

            <div class="field-wrapper">
                <label for="name">Nombre d'enceintes</label>
                <input type="number" id="name" v-model="nbSpeakers">
            </div>
        </div>

        <div class="column">
            <div class="validation-wrapper">
                <span class="validation-button" @click="createConfig">Valider</span>
            </div>
        </div>
    </div>
</template>

<script>
import FileSelection from '../../components/FileSelection.vue';
import emitter from '../../emitter';
import axiosInstance from '../../axiosInstance';

export default {
    name: 'NewConfig',
    components: {
        FileSelection
    },
    data() {
        return {
            name: '',
            nbLights: 0,
            nbSpeakers: 0
        }
    },
    methods: {
        /**
         * Creates a new config with the inputted informations
         */
        createConfig() {
            axiosInstance.post('/configs', {
                id: this.name,
                nbLights: this.nbLights,
                nbSpeakers: this.nbSpeakers
            }).then((response) => {
                // Set active config
                this.$store.commit('setActiveConfig', response.data);

                // Clear fields
                this.clearUI();

                // Refresh config list
                emitter.emit('fetchConfigs');
            }).catch((error) => {
                emitter.emit('error', error.response.data.error);
            });
        },

        /**
         * Clear UI fields (name, number of lights, number of speakers)
         */
        clearUI() {
            this.name = '';
            this.nbLights = 0;
            this.nbSpeakers = 0;

            emitter.emit('clearFileSelection'); // Clear file selection
            emitter.emit('error', ''); // Clear error message
        }
    }
}
</script>

<style scoped>
.wrapper {
    width: 100%;
    height: 100%;

    padding: 2% 2.5%;
}

.field-wrapper {
    display: flex;
    flex-direction: column;
}

.field-wrapper>input[type=text],
.field-wrapper>input[type=number] {
    width: 60%;
    padding: 2% 2.5%;
    border-radius: 7px;

    border: 0;
}

.field-wrapper>input:focus {
    outline: none;
    border: 0;
}

.column {
    width: 50%;
    height: 100%;
}

.column:last-of-type {
    display: flex;
    justify-content: flex-end;
    align-items: flex-end;
    flex-direction: column;
}

.column:first-of-type>div {
    margin-bottom: 1em;
}

.fileupload-wrapper {
    width: 25vw;
    height: 25vw;
}

.validation-wrapper {
    height: fit-content;
    display: flex;

    margin-top: 1em;
}

.validation-button {
    width: 100%;
    padding: 1em 4em;
    border-radius: 7px;

    transition-duration: 0.4s;
    background-color: #5b5b5b;
}

.validation-button:hover {
    cursor: pointer;
    filter: brightness(0.8);
}
</style>