<template>
    <div id="file-selector" @dragenter="dragAndDropHandler" @dragover="dragAndDropHandler" @drop="dragAndDropHandler"
        @dragleave="dragAndDropHandler" @click="clickHandler">
        <p v-if="!file">Déposez un fichier ou cliquez pour sélectionner</p>
        <p v-else>{{ file.name }}</p>
    </div>
</template>

<script>
import emitter from '../emitter.js';

export default {
    name: 'FileSelection',
    data() {
        return {
            file: null,
        };
    },
    props: {
        accept: {
            type: String,
            default: '*/*'
        }
    },
    mounted() {
        // Resets the file selection on event
        emitter.on('clearFileSelection', () => {
            this.file = null;
        });
    },
    methods: {
        /**
         * Handles the drag-and-drop event and prevents the default behavior.
         */
        dragAndDropHandler(event) {
            event.preventDefault();
            event.stopPropagation();

            // Change background color
            fileSelector.style.backgroundColor = '#000000';

            // Recover the file
            if (event.dataTransfer.items) {
                [...event.dataTransfer.items].forEach((item) => {
                    if (item.kind === 'file') {
                        this.file = item.getAsFile();
                        emitter.emit('fileImported', this.file)
                    }
                });
            } else {
                [...event.dataTransfer.files].forEach((file) => {
                    this.file = file;
                    emitter.emit('fileImported', this.file)
                });
            }
        },

        /**
         * Handles the click event and prevents the default behavior.
         */
        clickHandler(event) {
            event.preventDefault();
            event.stopPropagation();

            const input = document.createElement('input');
            input.type = 'file';
            input.accept = this.accept;
            input.onchange = () => {
                this.file = input.files[0];
                emitter.emit('fileImported', this.file)
            };
            input.click();
        },
    }
}
</script>

<style scoped>
#file-selector {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    border: 4px dashed #000000;
    border-radius: 15px;

    transition-duration: 0.4s;
    text-align: center;
}

#file-selector>p {
    font-weight: bold;
}

#file-selector:hover {
    background-color: #5b5a5a;
    cursor: pointer;
}
</style>