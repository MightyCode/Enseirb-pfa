<template>
    <div id="wrapper">
        <div class="waveform-wrapper">
            <div class="spinner-wrapper" v-show="this.loading">
                <scale-loader :loading="this.loading"></scale-loader>
            </div>

            <div id="waveform"></div>
        </div>

        <div class="toolbox">
            Toolbox here
        </div>

        <div class="timelines-wrapper">
            <div id="lights-timeline" class="timeline">
                Lights timeline here
            </div>

            <div id="speakers-timeline" class="timeline">
                Speakers timeline here
            </div>
        </div>
    </div>
</template>

<script>
import axiosInstance from '../axiosInstance';

export default {
    name: 'EditProject',
    data() {
        return {
            loading: true
        }
    },
    mounted() {
        const waveform = document.getElementById('waveform');
        const wavesurfer = WaveSurfer.create({
            container: waveform,
            waveColor: 'blue',
            progressColor: 'lightblue',
            plugins: [
                WaveSurfer.regions.create({})
            ]
        });

        axiosInstance.get('/static/audios/Metallica –The_unforgiven_3.mp3', {
            responseType: 'blob'
        }).then(response => {
            const blob = new Blob([response.data], { type: 'audio/mpeg' });
            const url = URL.createObjectURL(blob);

            wavesurfer.load(url);
        });

        wavesurfer.enableDragSelection({});

        wavesurfer.on('ready', () => {
            this.loading = false;
            waveform.style.opacity = 1;
        });

        // Handle region creation on click and drag
        let region;

        const deleteRegion = () => {
            if (region) {
                region.remove();
                region = null;
            }
        };

        wavesurfer.on('region-created', function (newRegion) {
            deleteRegion();
            // When a new region is created, set it as the active region
            region = newRegion;

            // Set the region's color
            region.update({ color: 'rgba(255, 0, 0, 0.2)' });
        });

        // Delete region on click anywhere
        wavesurfer.on('interaction', deleteRegion);
    }
}
</script>

<style scoped>
#wrapper {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

#waveform {
    opacity: 0;
}

.waveform-wrapper {
    width: 100%;
    height: 20%;

    display: flex;
    flex-direction: column;

    justify-content: center;
    position: relative;
}

.timeline {
    width: 100%;
    height: 45%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    background-color: red;
}

.timelines-wrapper {
    width: 100%;
    height: 60%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.toolbox {
    width: 100%;
    height: 10%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    background-color: red;
}

.spinner-wrapper {
    width: 100%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    position: absolute;
}
</style>