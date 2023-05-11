<template>
    <div class="wrapper">
        <div id="timeline" :style="timelineStyle">
            <div class="frame" v-for="(frame, index) in frames" :key="index.key" @click="selectedFrame = index"
                :style="{ 'background-color': index == selectedFrame ? '#3b3b3b' : '#5b5b5b' }" :draggable="true"
                @dragstart="dragStart(index)" @dragend="dragEnd" @drop="drop(index)" @dragover.prevent>
                <div class="frame-content">
                    <div class="frame-content-title">
                        {{ frame.key }}
                    </div>
                </div>
            </div>

        </div>

        <div class="buttons-wrapper">
            <button class="add-button button" @click="createFrame">+</button>
            <button class="remove-button button" @click="removeFrame">-</button>
        </div>

        <div class="effect-board">
            <div class="light-selection-list">
                <p v-if="selectedFrame !== -1" v-for="light in frames[selectedFrame].lights" class="selected-light">
                    {{ light }}
                </p>
            </div>

            <div id="viewer-wrapper">
                <p>Sélection des lumières</p>

                <div class="lights-wrapper" v-if="frames[selectedFrame]">
                    <div v-for="light in activeConfig.nbLights" :key="light">
                        <input :name="'light-' + light" type="checkbox" :value="light"
                            v-model="frames[selectedFrame].lights">
                        <label :for="'light-' + light">{{ light }}</label>
                    </div>
                </div>
            </div>
        </div>

        <div class="toolbox" v-if="frames[selectedFrame]">
            <div>
                <p>Couleur de la frame</p>
                <input type="color" v-model="frames[selectedFrame].color" />
            </div>
            <div>
                <p>Durée de la frame</p>
                <input type="number" v-model="frames[selectedFrame].length" />
                <p>ms</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "VisualEffectEdition",
    props: {
        effect: Object
    },
    data() {
        return {
            selectedFrame: -1,
            frames: [],

            dragIndex: null,
            dropIndex: null,
            frameCounter: 0,
        };
    },
    methods: {

        // === Required for frame drag and drop ===

        dragStart(index) {
            this.dragIndex = index;
        },
        drop(index) {
            this.dropIndex = index;
            const item = this.frames.splice(this.dragIndex, 1)[0];
            this.frames.splice(this.dropIndex, 0, item);
        },
        dragEnd() {
            this.dragIndex = null;
            this.dropIndex = null;
        },

        // === End of drag and drop ===

        /**
         * Creates a new frame and adds it to the frames array
         */
        createFrame() {
            this.frames.push({
                key: this.frameCounter++,
                lights: [],
                color: "#000000",
                length: 1,
            });

            this.selectedFrame = this.frames.length - 1;
        },

        /**
         * Removes the selected frame
         */
        removeFrame() {
            if (this.selectedFrame > -1) {
                this.frames.splice(this.selectedFrame, 1);
                this.selectedFrame = -1;
            } else if (this.frames.length > 0) {
                this.frames.pop();
            } else {
                console.warn("[VisualEffectEdition.vue] No frame to remove");
            }
        },
    },
    mounted() {       
        // Load existing frames and set the frame counter 
        if (this.effect.frames) {
            this.frames = this.effect.frames;
            this.frameCounter = this.frames.length;
        } else {
            this.effect.frames = [];
        }
    },
    unmounted() {
        // Store frames
        this.effect.frames = this.frames;
    },
    computed: {
        /**
         * VueX activeProject getter
         */
        activeProject() {
            return this.$store.state.activeProject;
        },

        /**
         * Compute the frame width
         */
        timelineStyle() {
            const size = 100 / this.frames.length;

            return {
                '--timeline-element-width': size + "%",
            };
        },

        /**
         * VueX activeConfig getter
         */
        activeConfig() {
            return this.$store.state.activeConfig;
        }
    }
}
</script>

<style scoped>
#timeline {
    width: 100%;
    height: 6em;
    overflow-y: auto;

    display: flex;
    flex-direction: row;
    padding: 0 1em;
}

div.wrapper {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;

    padding: 0;
}

.buttons-wrapper>.button {
    padding: .2em 1em;

    border-radius: 7px;
    border: none;
    background-color: #5b5b5b;
    color: white;
    font-size: 1em;
    font-weight: bold;

    transition-duration: 0.4s;
    margin-right: 1em;
}

.buttons-wrapper {
    margin: 0.5em 0;
}

.buttons-wrapper>.button:hover {
    background-color: #3b3b3b;
    cursor: pointer;
}

.effect-board {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 1em;

    flex: 1;
}

.light-selection-list {
    width: 20%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;

    background-color: #5b5b5b;
    overflow-y: auto;
    border-radius: 7px;
}

#viewer-wrapper {
    height: 100%;
    width: 80%;
}

#viewer-wrapper>p {
    margin: 0;
    padding: 0 0 0.5em 0;
    text-align: center;
    font-size: 1.2em;
    font-weight: bold;
    color: white;
}

.frame {
    height: 100%;
    width: var(--timeline-element-width);
    min-width: 2em;
    background-color: #5b5b5b;
    transition-duration: 0.4s;
    margin-right: 0.5em;
    border-radius: 7px;
}

.frame:last-of-type {
    margin-right: 0;
}

.frame:hover {
    background-color: #3b3b3b;
    cursor: pointer;
}

.frame-content-title {
    padding: 1%;
}

.selected-light {
    background-color: #3b3b3b;
    width: 80%;
    padding: 0.5em;
    text-align: center;
    border-radius: 7px;
    margin-bottom: 0;
    margin-top: 0.5em;
}

.toolbox {
    height: 3em;
    width: 100%;
    background-color: #5b5b5b;
    margin-top: 1em;

    display: flex;
    justify-content: space-evenly;
    border-radius: 7px;
}

.toolbox>div {
    display: flex;
    align-items: center;
}

.toolbox>div>p {
    margin: 0 1em;
}

.lights-wrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex-wrap: wrap;

    max-height: 85%;
    padding: 1em;
    overflow-x: auto;
}
</style>