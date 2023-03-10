<template>
    <div class="wrapper">
        <div class="column">
            <div class="field-wrapper">
                <label for="name">Name</label>
                <input type="text" id="name" v-model="name">
            </div>
        </div>

        <div class="column">
            <div class="fileupload-wrapper">
                <FileSelection accept="audio/*" />
            </div>

            <div class="validation-wrapper">
                <span class="validation-button" @click="createProject">Validate</span>
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
            filename: ''
        }
    },
    mounted() {
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
                audio: this.filename
            }).then((response) => {
                // Set active project
                this.$store.commit('setActiveProject', response.data);

                // Clear fields
                this.name = '';
                this.filename = '';
                emitter.emit('clearFileSelection');
                emitter.emit('error', '');

                // Refresh project list
                emitter.emit('fetchProjects');
            }).catch((error) => {
                emitter.emit('error', error.response.data.error);
            });
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
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.fileupload-wrapper {
    width: 25vw;
    height: 25vw;

    background-color: green;
}

.validation-wrapper {
    height: fit-content;
    display: flex;

    margin-top: 1em;
}

.validation-button {
    width: 100%;
    background-color: red;
    padding: 1em 4em;
    border-radius: 7px;

    transition-duration: 0.4s;
}

.validation-button:hover {
    cursor: pointer;
    filter: brightness(0.8);
}
</style>