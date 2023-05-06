<template>
    <div class="wrapper">
        <div class="column">
            <div class="field-wrapper">
                <label for="name">Nom</label>
                <input type="text" id="name" v-model="name">
            </div>
        </div>

        <div class="column">
            <h2>Audio</h2>
            <div class="fileupload-wrapper">
                <FileSelection accept="audio/*" />
            </div>

            <div class="validation-wrapper">
                <span :class="(name !== '' && filename !== '') ? 'validation-button' : 'validation-button-disabled'" @click="createProject">Valider</span>
            </div>
        </div>
    </div>
</template>

<script>
import FileSelection from '../../components/FileSelection.vue';
import emitter from '../../emitter';
import axiosInstance from '../../axiosInstance';

export default {
    name: 'NewProject',
    components: {
        FileSelection
    },
    data() {
        return {
            name: '',
            filename: '',
            config: null
        }
    },
    mounted() {
        this.config = this.activeConfig.id;
        
        emitter.on('fileImported', (file) => {
            const formData = new FormData();
            formData.append('file', file);

            axiosInstance.post('/audios', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then((response) => {
                this.filename = response.data.filename;
            }).catch((error) => {
                emitter.emit('error', error.response.data.error);
                this.filename = error.response.data.filename;
            });
        });
    },
    methods: {
        createProject() {
            axiosInstance.post('/projects', {
                id: this.name,
                audio: this.filename,
                config: this.config
            }).then((response) => {
                // Set active project
                this.$store.commit('setActiveProject', response.data);

                // Clear fields
                this.clearUI();

                // Refresh project list
                emitter.emit('fetchProjects');
            }).catch((error) => {
                emitter.emit('error', error.response.data.error);
            });
        },

        clearUI() {
            this.name = '';
            this.filename = '';
            emitter.emit('clearFileSelection');
            emitter.emit('error', '');
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
label {
    font-size: 1em;
    font-weight: bolder;
    margin-bottom: 0.2em;
}
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

.column > h2 {
    margin: 0;
}

.column:last-of-type {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;
}

.fileupload-wrapper {
    width: 20vw;
    height: 20vw;
}

.validation-wrapper {
    height: fit-content;
    width: 100%;
    display: flex;

    margin-top: 1em;
    justify-content: flex-end;
}

.validation-button {
    width: fit-content;
    padding: 1em 4em;
    border-radius: 7px;

    transition-duration: 0.4s;
    background-color: #5b5b5b;
}

.validation-button-disabled {
    width: fit-content;
    padding: 1em 4em;
    border-radius: 7px;

    transition-duration: 0.4s;
    background-color: #3b3b3b;
}

.validation-button:hover {
    cursor: pointer;
    filter: brightness(0.8);
}
</style>