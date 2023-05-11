<template>
    <div id="wrapper">
        <!-- <div class="waveform-wrapper">
            <div class="spinner-wrapper" v-show="this.loading">
                <scale-loader :loading="this.loading"></scale-loader>
            </div>

            <div id="waveform"></div>
        </div> -->

        
        <!-- <div class="timelines-wrapper"> -->
            

            <div class="timeline" id="timeline">
                <!-- Add this element inside the timeline container -->
            <div class="timeline-line"></div>
                <!-- Timeline marker -->
                <div class="timeline-marker" id="timeline-marker"></div>
            <!-- </div> -->
        </div>
    </div>
</template>

<script>

import axiosInstance from '../axiosInstance';

export default {
    name: 'VisualizeProject',
    data() {
        return {
            loading: true
        }
    },
    mounted() {
        
        
        var ctx = document.createElement('canvas').getContext('2d');
        var linGrad = ctx.createLinearGradient(0, 64, 0, 200);
        linGrad.addColorStop(0.5, 'rgba(255, 255, 255, 1.000)');
        linGrad.addColorStop(0.5, 'rgba(183, 183, 183, 1.000)');

        const waveform = document.getElementById('waveform');
        const wavesurfer = WaveSurfer.create({
            container: waveform,
            waveColor: linGrad,
            plugins: [
                WaveSurfer.regions.create({})
            ],
            progressColor: 'hsla(200, 100%, 30%, 0.5)',
            // This parameter makes the waveform look like SoundCloud's player
            barWidth: 3
        });

        // Load current project's audio
        axiosInstance.get(`/static/audios/${this.activeProject.audio}`, {
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
    },
    computed: {
        activeProject() {
            return this.$store.state.activeProject;
        }
    }
}

// const json = {
// 		    "audioTimeline": [
// 		        {
// 		            "name": "boom1",
// 		            "start": 0,
// 		            "priority": 1,
// 		            "audioStreamOut": 0,
// 		            "modelEffect": {
// 		                "name": "play",
// 		                "file": "interface/python/audio/sound/retro.wav",
// 		                "amplitude": 1,
// 		                "loopTime": 5
// 		            }
// 		        },
// 		        {
// 		            "name": "meuh2",
// 		            "start": 1.6667,
// 		            "priority": 1,
// 		            "audioStreamIn": 0,
// 		            "audioStreamOut": [0, 1],
// 		            "modelEffect": {
// 		                "name": "split",
// 		                "length": 3.4
// 		            }
// 		        },
// 		        {
// 		            "name": "meuh3",
// 		            "start": 1.6,
// 		            "priority": 1,
// 		            "audioStreamOut": 1,
// 		            "modelEffect": {
// 		                "name": "mute",
// 		                "length": 2.4
// 		            }
// 		        }
// 		    ]
// 		};

// 		const data = json;
// 		const timeline = document.getElementById("timeline");
// 		const timelineMarker = document.getElementById("timeline-marker");

// 		// Create the event box container
// 		let previousEventBox;
// 		// Loop through the events in the data and create event boxes
// for (let i = 0; i < data.audioTimeline.length; i++) {
// const event = data.audioTimeline[i];
// // Create a new event box element
// // Create a new event box element
// const eventBox = document.createElement("div");
// eventBox.classList.add("event-box");

// // Check for interference and add a class to the event box
// if (event.audioStreamOut && Array.isArray(event.audioStreamOut)) {
//     eventBox.classList.add("interference");
// }

// // Set the event box position based on the start time
// const leftPos = event.start * 25 + "%";
// eventBox.style.left = leftPos;

// // Set the event box content
// eventBox.innerHTML = `
//     <div class="event-name">${event.name}</div>
//     <div class="event-start">Start: ${event.start}</div>
//     <div class="event-priority">Priority: ${event.priority}</div>
// `;

// // Add the event box to the timeline container
// timeline.appendChild(eventBox);



// // Update the previous event box to current box
// previousEventBox = eventBox;

// // Store the end time of the current event box for use in the next connector
// eventBox.dataset.end = event.start;

// 	}

// 	// Set the position of the timeline marker based on the current time
// 	const currentTime = Date.now() / 1000; // Convert to seconds
// 	const timelineWidth = timeline.offsetWidth;
// 	const markerLeft = (currentTime / data.audioTimeline[data.audioTimeline.length - 1].start) * timelineWidth;
// 	timelineMarker.style.left = markerLeft + "px";

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

/* Style the timeline container */
.timeline {
    position: relative;
    height: 200px; /* Increase the height to fit all the event boxes */
    margin: 20px;
    border: 1px solid #ccc;
    background-color: #f2f2f2;
    overflow-x: scroll;
    overflow-y: hidden;
}
.event-box.interference {
top: 60px; /* Adjust this value to move the box down */
}
.connector {
    position: absolute;
    height: 2px;
    background-color: #ccc;
    top: 30px; /* Adjust this value to center the line */
}
/* Style the event boxes */
.event-box {
    position: absolute;
    width: 150px;
    height: 50px;
    background-color: #eee;
    border: 1px solid #ccc;
    margin: 5px;
    padding: 10px;
    text-align: center;
    font-size: 12px;
    line-height: 1.2;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    cursor: pointer;
}
/* Style the event name */
.event-name {
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 5px;
}
/* Style the event start time */
.event-start {
    font-size: 12px;
    color: #666;
    margin-bottom: 5px;
}
/* Style the event priority */
.event-priority {
    font-size: 12px;
    color: #666;
    margin-bottom: 5px;
}
.timeline-line {
position: absolute;
top: 50%;
left: 0;
width: 100%;
height: 1px;
background-color: #000000;
z-index: 0; /* set a lower z-index so the line appears behind the event boxes */
}

.timelines-wrapper {
    width: 100%;
    height: 60%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
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