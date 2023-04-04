<template>
    <div class="wrapper">
        <div id="timeline" :style="timelineStyle">
            <div class="frame" v-for="(frame, index) in frames" 
                :key="index.key" 
                @click="selectedFrame = index" 
                :style="{ 'background-color': index == selectedFrame ? 'red': 'white'}"
                :draggable="true"
                @dragstart="dragStart(index)"
                @dragend="dragEnd"
                @drop="drop(index)"
                @dragover.prevent
                >
                <div class="frame-content">
                    <div class="frame-content-title">
                        Frame {{ frame.key }}
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
                <div id="viewer">

                </div>
            </div>
        </div>

        <div class="toolbox">

        </div>
    </div>
</template>

<script>
export default {
    name: "VisualEffectEdition",
    data() {
        return {
            selectedFrame: -1,
            stage: null,
            frames: [],

            dragIndex: null,
            dropIndex: null,
            frameCounter: 0,
        };
    },
    methods: {
        dragStart(index) {
            console.log("Drag at index " + index)
            this.dragIndex = index;
        },
        drop(index) {
            console.log("Drop at index " + index)
            this.dropIndex = index;
            const item = this.frames.splice(this.dragIndex, 1)[0];
            this.frames.splice(this.dropIndex, 0, item);
        },
        dragEnd() {
            this.dragIndex = null;
            this.dropIndex = null;
        },
        createFrame() {
            this.frames.push({
                key: this.frameCounter++,
                lights: [],
                color: "#000000"
            });

            this.selectedFrame = this.frames.length - 1;
        },
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
        loadFromProject() {
            if (!this.activeProject.konvaEnv) {
                console.info("[VisualEffectEdition.vue] No Konva environment found in the active project");
                return;
            }

            this.stage = Konva.Node.create(this.activeProject.konvaEnv.json, "viewer");

            this.deletedLightsIds = JSON.parse(this.activeProject.konvaEnv.deletedLightsIds);
            this.deletedSpeakersIds = JSON.parse(this.activeProject.konvaEnv.deletedSpeakersIds);

            this.speakersCounter = this.activeProject.konvaEnv.speakersCounter;
            this.lightsCounter = this.activeProject.konvaEnv.lightsCounter;

            this.fitStageIntoParentContainer();

            // Find clicked element 
            const layer = this.stage.getChildren()[0];
            const clickables = layer.getChildren();

            // Add event listeners
            clickables.forEach(clickable => {
                // Disable draggability
                clickable.draggable(false);

                if (clickable.getId().split('-')[0] !== "light") {
                    return;
                }

                clickable.on("mousedown", () => {
                    if (this.selectedFrame == -1) {
                        return;
                    }

                    // TTurn children without 'textWidth' property into blue
                    clickable.getChildren().forEach(child => {
                        if (!child.textWidth) {
                            this.frames[this.selectedFrame].lights.push(clickable.getId());
                        }
                    });
                });

                // Add hover effect
                clickable.on("mouseover", () => {
                    document.body.style.cursor = "pointer";
                });

                clickable.on("mouseout", () => {
                    document.body.style.cursor = "default";
                });
            });


        },

        fitStageIntoParentContainer() {
            const wrapper = document.querySelector("#viewer-wrapper");

            // Get parent's width
            const containerWidth = wrapper.offsetWidth;
            const containerHeight = wrapper.offsetHeight;

            this.stage.height(containerHeight);
            this.stage.width(containerWidth);
            this.stage.draw();
        }
    },
    mounted() {
        const sceneWidth = 800;
        const sceneHeight = 400;

        this.stage = new Konva.Stage({
            container: "viewer",
            width: sceneWidth,
            height: sceneHeight,
            id: "stage",
        });

        this.stage.add(new Konva.Layer({ id: "layer" }));

        // Adapt the stage on resize
        window.addEventListener("resize", this.fitStageIntoParentContainer);


        this.loadFromProject();
        this.stage.scale({ x: 1, y: 1 });
    },
    computed: {
        activeProject() {
            return this.$store.state.activeProject;
        },
        timelineStyle() {
            const size = 100 / this.frames.length;

            return {
                '--timeline-element-width': size + "%",
            };
        }
    }
}
</script>

<style scoped>
#timeline {
    background-color: red;
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
}

#viewer-wrapper {
    height: 100%;
    width: 80%;
}

.frame {
    height: 100%;
    width: var(--timeline-element-width); 
    background-color: #5b5b5b;
    border: 1px solid #ff0000;
    transition-duration: 0.4s;
}

.frame:hover {
    background-color: #3b3b3b;
    cursor: pointer;
}

.selected-light {
    background-color: #3b3b3b;
    width: 80%;
    padding: 0.5em;
    text-align: center;
    border-radius: 7px;
    margin-bottom: 0;
}

.toolbox {
    height: 3em;
    width: 100%;
    background-color: red;
    margin-top: 1em;
}
</style>