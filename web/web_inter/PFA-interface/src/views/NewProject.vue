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
                            <input type="text" placeholder="Ex: Eirlab-Crémaillère" name="project-name">
                        </div>

                        <div class="row">
                            <label for="nb-lights">Nombre lumières</label>
                            <input type="number" placeholder="Ex: 54" name="nb-lights">
                        </div>

                        <div class="row">
                            <label for="nb-speakers">Nombre enceintes</label>
                            <input type="number" placeholder="Ex: 10" name="nb-speakers">
                        </div>
                    </section>

                    <section>
                        <div class="row">
                            <FileSelection />
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

section:last-of-type {
    width: 20vw;
    height: 20vw;
}

section:last-of-type>div {
    width: 100%;
    height: 100%;
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
</style>