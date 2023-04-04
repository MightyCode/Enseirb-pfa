<template>
    <div class="edition-wrapper">
        <div class="row">
            <span>Édition / Création d'un effet</span>
        </div>
        <div class="row">
            <div>
                <label for="effect-name">Nom</label>
                <input type="text" name="effect-name" id="effect-name">
            </div>

            <div>
                <label for="effect-type">Type</label>
                <select name="effect-type" v-model="effect.type">
                    <option>AUDIO</option>
                    <option>LIGHT</option>
                </select>
            </div>
        </div>

        <div class="row">
            <AudioEffectEdition v-if="effect.type === 'AUDIO'" />
            <VisualEffectEdition v-if="effect.type === 'LIGHT'" />
        </div>
    </div>
</template>

<script>
import AudioEffectEdition from '../components/effects/AudioEffectEdition.vue';
import VisualEffectEdition from '../components/effects/VisualEffectEdition.vue';

export default {
    name: "EditEffect",
    props: {
        effect: Object
    },
    data() {
        return {
            effectType: "AUDIO"
        }
    },
    components: {
        AudioEffectEdition,
        VisualEffectEdition
    }
}
</script>

<style scoped>
div.edition-wrapper {
    width: 80%;
    height: 100%;

    display: flex;
    flex-direction: column;

    padding: 0.5em 2em;
}

.edition-wrapper>.row {
    width: 100%;
    height: 9%;

    display: flex;
    flex-direction: row;
    align-items: center;

    margin-bottom: 1%;
}

.edition-wrapper>.row:last-of-type {
    height: 80%;
    margin-bottom: 0;
}

.edition-wrapper>.row>span {
    font-size: 1.5em;
    font-weight: bold;
}


.edition-wrapper>.row>div {
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;

    margin: 0 1em;
}

.edition-wrapper>.row>div:first-of-type {
    margin-left: 0;
}

.edition-wrapper>.row>div:last-of-type {
    margin-right: 0;
}

.edition-wrapper>.row>div>input,
.edition-wrapper>.row>div>select {
    width: 30em;
    height: 3em;

    padding: 0 1em;
    border-radius: 7px;

    border: 0;
}

.edition-wrapper>.row>div>input:focus,
.edition-wrapper>.row>div>select:focus {
    outline: none;
    border: 0;
}

.red {
    background-color: red;
}

.blue {
    background-color: blue;
}

.green {
    background-color: green;
}
</style>