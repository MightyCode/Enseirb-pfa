<template>
    <div id="wrapper">
        <div id="viewer" />
    </div>
    <footer>
        <div @click="resetEnvironment" class="button">
            <p>Reset</p>
        </div>

        <div @click="saveEnvironment" class="button">
            <p>Save</p>
        </div>
    </footer>
</template>

<script>
export default {
    name: "ConfigEnv",
    data() {
        return {
            stage: null,

            deletedLightsIds: [],
            deletedSpeakersIds: [],

            speakersCounter: 0,
            lightsCounter: 0,

            circleDiameter: 20
        };
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

        const fitStageIntoParentContainer = () => {
            const wrapper = document.querySelector("#wrapper");

            // Get parent's width
            const containerWidth = wrapper.offsetWidth;
            const containerHeight = wrapper.offsetHeight;

            // To do this we need to scale the stage
            const scale = containerWidth / sceneWidth;

            this.stage.width(containerWidth);
            this.stage.height(containerHeight);
            this.stage.scale({ x: scale, y: scale });
            this.stage.draw();
        }

        fitStageIntoParentContainer();

        // Adapt the stage on resize
        window.addEventListener("resize", fitStageIntoParentContainer);

        // On left click
        this.stage.on("mousedown", this.handleLeftClick);

        // On right click, add a speaker at the mouse position
        this.stage.on("contextmenu", this.handleRightClick);


        this.stage.draw();

        this.loadFromProject();
    },
    methods: {
        /**
         * Gets the actual mouse position inside the Konva stage
         */
        getMousePos() {
            const mousePos = this.stage.getPointerPosition();

            mousePos.x /= this.stage.scaleX();
            mousePos.y /= this.stage.scaleY();
            mousePos.x -= this.stage.x() / this.stage.scaleX();
            mousePos.y -= this.stage.y() / this.stage.scaleY();

            return mousePos;
        },

        /**
         * Gets the next available light id
         * Takes into account the deleted lights ids
         */
        getNextLightId() {
            if (this.deletedLightsIds.length > 0) {
                return this.deletedLightsIds.pop();
            }

            return this.lightsCounter++;
        },

        /**
         * Gets the next available speaker id
         * Takes into account the deleted speakers ids
         */
        getNextSpeakerId() {
            if (this.deletedSpeakersIds.length > 0) {
                return this.deletedSpeakersIds.pop();
            }

            return this.speakersCounter++;
        },

        /**
         * Clears all created lights and speakers
         */
        resetEnvironment() {
            this.stage.destroyChildren();

            const layer = new Konva.Layer();
            this.stage.add(layer);

            this.stage.draw();

            this.lightsCounter = 0;
            this.speakersCounter = 0;
            this.deletedLightsIds = [];
            this.deletedSpeakersIds = [];
        },

        /**
         * Load the environment from the VueX store's active project
         */
        loadFromProject() {
            if (!this.activeProject.konvaEnv) {
                console.info("[ConfigEnv.vue] No Konva environment found in the active project");
                return;
            }

            this.resetEnvironment();

            // Remove event listeners
            this.stage.removeEventListener("mousedown", this.handleLeftClick);
            this.stage.removeEventListener("contextmenu", this.handleRightClick);

            this.stage = Konva.Node.create(this.activeProject.konvaEnv.json, "viewer");

            // Add event listeners
            this.stage.on("mousedown", this.handleLeftClick);
            this.stage.on("contextmenu", this.handleRightClick);

            this.stage.draw();

            this.deletedLightsIds = JSON.parse(this.activeProject.konvaEnv.deletedLightsIds);
            this.deletedSpeakersIds = JSON.parse(this.activeProject.konvaEnv.deletedSpeakersIds);

            this.speakersCounter = this.activeProject.konvaEnv.speakersCounter;
            this.lightsCounter = this.activeProject.konvaEnv.lightsCounter;
        },

        /**
         * Save the environment to the VueX store's active project as a JSON string
         */
        saveEnvironment() {
            const projectToSave = {
                ...this.activeProject,
                konvaEnv: {
                    json: this.stage.toJSON(),

                    deletedLightsIds: JSON.stringify(this.deletedLightsIds),
                    deletedSpeakersIds: JSON.stringify(this.deletedSpeakersIds),

                    speakersCounter: this.speakersCounter,
                    lightsCounter: this.lightsCounter,
                },
            };

            this.$store.dispatch("setActiveProject", projectToSave);
        },

        handleLeftClick(e) {
            // Check if right click
            if (e.evt.button === 2) {
                return;
            }

            // Get first layer
            const layer = this.stage.getLayers()[0];

            // If the click is not on a Konva element, add a light at the mouse position
            if (e.target.getId() === this.stage.getId()) {

                console.log("add light")
                const mousePos = this.getMousePos();

                const light = new Konva.Circle({
                    x: mousePos.x,
                    y: mousePos.y,
                    radius: this.circleDiameter / 2,
                    fill: "yellow",
                    stroke: "black",
                    strokeWidth: 1,
                    height: this.circleDiameter,
                    width: this.circleDiameter,
                });

                const id = this.getNextLightId();

                // Pseudo-padding to center the id
                const xModifier = (id + 1).toString().length > 1 ? 4 : 7;

                // Add the light's id
                const text = new Konva.Text({
                    x: light.x() - (this.circleDiameter / 2) + xModifier,
                    y: light.y() - (this.circleDiameter / 2) + 4,
                    text: id,
                    fontSize: 12,
                    fontFamily: "Calibri",
                    fill: "black",
                });

                // Group the light and the id in a draggable group
                const group = new Konva.Group({
                    draggable: true,
                    id: `light-${id}`
                });

                group.add(light);
                group.add(text);

                layer.add(group);
            }

            this.stage.draw();
        },

        handleRightClick(e) {
            e.evt.preventDefault();

            // Get first layer
            const layer = this.stage.getLayers()[0];

            if (e.target.getId() === this.stage.getId()) {
                const mousePos = this.getMousePos();
                const id = this.getNextSpeakerId();

                // Create the speaker
                const speaker = new Konva.Circle({
                    x: mousePos.x,
                    y: mousePos.y,
                    radius: this.circleDiameter / 2,
                    fill: "red",
                    stroke: "black",
                    strokeWidth: 1,
                    height: this.circleDiameter,
                    width: this.circleDiameter,
                });


                // Pseudo-padding to center the id
                const xModifier = (id + 1).toString().length > 1 ? 4 : 7;

                // Add the speaker's id
                const text = new Konva.Text({
                    x: speaker.x() - (this.circleDiameter / 2) + xModifier,
                    y: speaker.y() - (this.circleDiameter / 2) + 4,
                    text: id,
                    fontSize: 12,
                    fontFamily: "Calibri",
                    fill: "black",
                });

                // Group the speaker and the id in a draggable group
                const group = new Konva.Group({
                    draggable: true,
                    id: `speaker-${id}`
                });

                group.add(speaker);
                group.add(text);

                layer.add(group);
            }
            // If the click is on a Konva element, delete the group containing the element
            else {
                const group = e.target.getParent();

                // Get the id of the deleted light or speaker
                const id = parseInt(group.children[1].text());

                // If the deleted element is a light, add its id to the deleted lights ids
                if (group.children[0].fill() === "yellow") {
                    this.deletedLightsIds.push(id);
                }

                // If the deleted element is a speaker, add its id to the deleted speakers ids
                if (group.children[0].fill() === "red") {
                    this.deletedSpeakersIds.push(id);
                }

                group.destroy();
            }

            this.stage.draw();
        }
    },
    computed: {
        activeProject() {
            return this.$store.state.activeProject;
        },
    }
}
</script>

<style scoped>
#wrapper {
    height: 90%;
    width: 100%;
}

#viewer {
    border: 1px solid black;
    height: 100%;
    width: 100%;
}

footer {
    height: 10%;
    width: 100%;

    display: flex;
    justify-content: flex-end;
    align-items: center;
}

.button {
    margin: 0 1em 0 0;
    background-color: #5b5b5b;
    padding: 0.75em 3em;

    height: fit-content;

    display: flex;
    justify-content: center;
    align-items: center;

    border-radius: 7px;

    transition-duration: 0.4s;
}

.button:hover {
    background-color: #3b3b3b;
    cursor: pointer;
}

.button>p {
    color: white;
    margin: 0;
}
</style>