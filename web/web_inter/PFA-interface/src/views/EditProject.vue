<template>
    <div id="wrapper">
        <div class="waveform-wrapper">
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
export default {
    name: 'EditProject',
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


        wavesurfer.load('/Metallica –The_unforgiven_3.mp3');
        wavesurfer.enableDragSelection({

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

.waveform-wrapper {
    width: 100%;
    height: 20%;

    display: flex;
    flex-direction: column;

    justify-content: center;
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
</style>