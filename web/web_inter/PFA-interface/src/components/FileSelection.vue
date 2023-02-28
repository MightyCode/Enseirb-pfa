<template>
    <div id="main">
        <p v-if="!file">Drag a file here or click to upload</p>
        <p v-else>{{ file.name }}</p>
    </div>
</template>

<script>
export default {
    name: 'FileSelection',
    data() {
        return {
            file: null,
        };
    },
    mounted() {
        const main = document.getElementById('main');
        const handler = e => {
            e.preventDefault();
            e.stopPropagation();

            // Change background color
            main.style.backgroundColor = '#000000';

            // Recover the file
            if (e.dataTransfer.items) {
                [...e.dataTransfer.items].forEach((item) => {
                    if (item.kind === 'file') {
                        this.file = item.getAsFile();
                    }
                });
            } else {
                [...e.dataTransfer.files].forEach((file) => {
                    this.file = file;
                });
            }
        };
        
        // Handle drag and drop
        main.addEventListener('dragenter', handler);
        main.addEventListener('dragover', handler);
        main.addEventListener('drop', handler);
        main.addEventListener('dragleave', handler);
    }
}
</script>

<style scoped>

#main {
    width: 100%;
    height: 100%;
    
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    border: 4px dashed #000000;
    border-radius: 15px;
}
</style>