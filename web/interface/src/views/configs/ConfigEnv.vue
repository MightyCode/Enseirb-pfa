<template>
    <div id="wrapper">
        <div id="viewer" />
    </div>
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
        };
    },
    mounted() {
        const sceneWidth = 800;
        const sceneHeight = 400;

        const stage = new Konva.Stage({
            container: "viewer",
            width: sceneWidth,
            height: sceneHeight,
        });

        const layer = new Konva.Layer();
        stage.add(layer);

        function fitStageIntoParentContainer() {
            const wrapper = document.querySelector("#wrapper");

            // Get parent's width
            const containerWidth = wrapper.offsetWidth;
            const containerHeight = wrapper.offsetHeight;

            // To do this we need to scale the stage
            const scale = containerWidth / sceneWidth;

            stage.width(containerWidth);
            stage.height(containerHeight);
            stage.scale({ x: scale, y: scale });
            stage.draw();
        }

        fitStageIntoParentContainer();

        // Adapt the stage on resize
        window.addEventListener("resize", fitStageIntoParentContainer);

        const circleDiameter = 20;

        let id = 0;

        // On left click
        stage.on("mousedown", (e) => {

            // Check if right click
            if (e.evt.button === 2) {
                return;
            }

            // If the click is not on a Konva element, add a light at the mouse position
            if (e.target === stage || e.target === layer) {
                const mousePos = this.getMousePos();

                const light = new Konva.Circle({
                    x: mousePos.x,
                    y: mousePos.y,
                    radius: circleDiameter / 2,
                    fill: "yellow",
                    stroke: "black",
                    strokeWidth: 1,
                    height: circleDiameter,
                    width: circleDiameter,
                });

                const id = this.getNextLightId();

                // Pseudo-padding to center the id
                const xModifier = (id + 1).toString().length > 1 ? 4 : 7;

                // Add the light's id
                const text = new Konva.Text({
                    x: light.x() - (circleDiameter / 2) + xModifier,
                    y: light.y() - (circleDiameter / 2) + 4,
                    text: id,
                    fontSize: 12,
                    fontFamily: "Calibri",
                    fill: "black",
                });

                // Group the light and the id in a draggable group
                const group = new Konva.Group({
                    draggable: true,
                });

                group.add(light);
                group.add(text);

                layer.add(group);
            }

            stage.draw();
        });

        // On right click, add a speaker at the mouse position
        stage.on("contextmenu", (e) => {
            e.evt.preventDefault();

            if (e.target === stage || e.target === layer) {
                const mousePos = this.getMousePos();

                // Create the speaker
                const speaker = new Konva.Circle({
                    x: mousePos.x,
                    y: mousePos.y,
                    radius: circleDiameter / 2,
                    fill: "red",
                    stroke: "black",
                    strokeWidth: 1,
                    height: circleDiameter,
                    width: circleDiameter,
                });

                const id = this.getNextSpeakerId();

                // Pseudo-padding to center the id
                const xModifier = (id + 1).toString().length > 1 ? 4 : 7;

                // Add the speaker's id
                const text = new Konva.Text({
                    x: speaker.x() - (circleDiameter / 2) + xModifier,
                    y: speaker.y() - (circleDiameter / 2) + 4,
                    text: id,
                    fontSize: 12,
                    fontFamily: "Calibri",
                    fill: "black",
                });

                // Group the speaker and the id in a draggable group
                const group = new Konva.Group({
                    draggable: true,
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

            stage.draw();
        });


        this.stage = stage;
        this.stage.draw();
    },
    methods: {
        getMousePos() {
            const mousePos = this.stage.getPointerPosition();

            mousePos.x /= this.stage.scaleX();
            mousePos.y /= this.stage.scaleY();
            mousePos.x -= this.stage.x() / this.stage.scaleX();
            mousePos.y -= this.stage.y() / this.stage.scaleY();

            return mousePos;
        },

        getNextLightId() {
            if (this.deletedLightsIds.length > 0) {
                return this.deletedLightsIds.pop();
            }

            return this.lightsCounter++;
        },

        getNextSpeakerId() {
            if (this.deletedSpeakersIds.length > 0) {
                return this.deletedSpeakersIds.pop();
            }

            return this.speakersCounter++;
        }
    }
}
</script>

<style scoped>
#wrapper {
    height: 100%;
    width: 100%;
}

#viewer {
    border: 1px solid black;
    height: 100%;
    width: 100%;
}
</style>