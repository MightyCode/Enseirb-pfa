<template>
    <fieldset>
        <legend>
            <p>Nouveau projet</p>
            <p>Informations générales</p>
        </legend>

        <div>
            <form>
                <div class="wrapper-row">
                    <section>
                        <div class="row">
                            <label for="project-name">Nom affiché</label>
                            <input type="text" placeholder="Ex: Eirlab-Crémaillère" name="project-name"
                                v-model="projectName">
                        </div>

                        <div class="row">
                            <label for="nb-lights">Nombre lumières</label>
                            <input type="number" placeholder="Ex: 54" name="nb-lights" v-model="nbLights">
                        </div>

                        <div class="row">
                            <label for="nb-speakers">Nombre enceintes</label>
                            <input type="number" placeholder="Ex: 10" name="nb-speakers" v-model="nbSpeakers">
                        </div>
                    </section>

                    <section>
                        <div class="row">
                            <FileSelection accept="audio/*"/>
                        </div>

                        <div class="row">
                            <div id="device-placement" />
                        </div>
                    </section>
                </div>
                <div class="wrapper-row">
                    <input type="button" value="Submit" class="tab-link" onclick="opentab('audiovis')">
                </div>
            </form>
        </div>

    </fieldset>
</template>

<script>
import FileSelection from '../components/FileSelection.vue'

export default {
    name: 'NewProject',
    components: {
        FileSelection
    },
    data() {
        return {
            projectName: '',
            nbLights: 0,
            nbSpeakers: 0,
            file: null,
            stage: null,
        }
    },
    mounted() {
        const sceneWidth = 800;
        const sceneHeight = 400;

        const stage = new Konva.Stage({
            container: 'device-placement',
            width: sceneWidth,
            height: sceneHeight,
        });

        const layer = new Konva.Layer();
        stage.add(layer);

        function fitStageIntoParentContainer() {
            const container = document.querySelector('#device-placement');

            // now we need to fit stage into parent
            const containerWidth = container.offsetWidth;
            // to do this we need to scale the stage
            const scale = containerWidth / sceneWidth;

            stage.width(sceneWidth * scale);
            stage.height(sceneHeight * scale);
            stage.scale({ x: scale, y: scale });
        }

        fitStageIntoParentContainer();

        // adapt the stage on any window resize
        window.addEventListener('resize', fitStageIntoParentContainer);

        this.stage = stage;
    },
    watch: {
        nbLights: function (newVal, oldVal) {
            // Clear Konva canvas
            this.stage.destroyChildren();
            const diameter = 20;

            const layer = new Konva.Layer();

            // Add new lights
            for (let i = 0; i < newVal; i++) {
                // Create a Konva.Circle instance
                // And display $i in the center of the circle
                const circle = new Konva.Circle({
                    x: 50 + (i * 50),
                    y: 50,
                    radius: diameter / 2,
                    fill: 'yellow',
                    stroke: 'black',
                    strokeWidth: 1,
                    height: diameter,
                    width: diameter,
                });

                const xModifier = (i + 1).toString().length > 1 ? 4 : 7;

                // Display the index of the light
                const text = new Konva.Text({
                    x: circle.x() - (diameter / 2) + xModifier,
                    y: circle.y() - (diameter / 2) + 4,
                    text: i + 1,
                    fontSize: 12,
                    fontFamily: 'Calibri',
                    fill: 'black',
                });

                const group = new Konva.Group({
                    draggable: true,
                });

                group.add(circle);
                group.add(text);

                // Add the shape to the layer
                layer.add(group);
            }

            this.stage.add(layer);
            this.stage.draw();
        },
    }
}
</script>

<style scoped>
.row {
    display: flex;
    flex-direction: column;
    margin-bottom: 1.5rem;
    color: #000000;
}

.row>label {
    padding-bottom: 0.1rem;
    padding-left: 0.5rem;

    font-weight: 500;
}

.row>input[type=text],
.row>input[type=number] {
    width: 60%;
    padding: 2% 2.5%;
    border-radius: 7px;

    border: 0;
}

.row>input:focus {
    outline: none;
    border: 0;
}

form {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
}

form>.wrapper-row {
    display: flex;
    flex-direction: row;
}

.wrapper-row:first-of-type {
    height: 90%;
}

.wrapper-row:last-of-type {
    height: 10%;
    justify-content: flex-end;
}

.wrapper-row>section {
    width: 50%;
    height: 100%;
}

section:last-of-type {}

section:last-of-type>.row:first-of-type {
    width: 100%;
    height: 20%;
}

section:last-of-type>.row:last-of-type {
    width: 100%;
    height: 80%;
}

/* ========================================= */

fieldset {
    border: 3px solid #000000;
    padding: 1%;

    height: 100%;
}

fieldset>legend {
    width: 20%;

    display: flex;
    flex-direction: column;

    padding: 0 1%;
    color: black
}

fieldset>legend>p:first-of-type {
    font-size: 2em;
    padding: 0 1%;
    font-weight: bolder;
    margin: 0;
}

fieldset>legend>p:last-of-type {
    font-size: 1em;
    padding: 0 1%;
    font-weight: bold;
    margin-top: 0;
}

fieldset>div {
    width: 100%;
    height: 100%;
}

#device-placement {
    border: 1px solid black;
}
</style>