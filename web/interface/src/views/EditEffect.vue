<template>
    <div class="edition-wrapper">
        <div class="row">
            <span>Édition / Création d'un effet</span>
        </div>
        <div class="row">
            <div>
                <label for="effect-name">Nom</label>
                <input type="text" name="effect-name" id="effect-name" v-model="effect.name">
            </div>

            <div>
                <label for="effect-type">Type</label>
                <select name="effect-type" v-model="effect.type">
                    <option>AUDIO</option>
                    <option>LIGHT</option>
                </select>
            </div>

            <div class="delete-button" @click="onDeleteButtonClick">
                <span>Supprimer</span>
            </div>
        </div>

        <div class="row">
            <AudioEffectEdition v-if="effect.type === 'AUDIO'" :effect="effect" />
            <VisualEffectEdition v-if="effect.type === 'LIGHT'" :effect="effect" />
        </div>
    </div>
</template>

<script>
import AudioEffectEdition from '../components/effects/AudioEffectEdition.vue';
import VisualEffectEdition from '../components/effects/VisualEffectEdition.vue';
import axiosInstance from '../axiosInstance';
import emitter from '../emitter';

export default {
    name: "EditEffect",
    props: {
        effect: Object
    },
    data() {
        return {
            effectType: "AUDIO",
            isEffectDeleted: false
        }
    },
    components: {
        AudioEffectEdition,
        VisualEffectEdition
    },
    unmounted() {
        // Avoid effect being saved just after being deleted
        if (this.isEffectDeleted) {
            return;
        }

        // PUT at /effects/<id>
        axiosInstance.put('/effects/' + this.effect.id, this.effect)
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            });
    },
    mounted() {
        // Avoid effect being saved just after being deleted
        emitter.on('effect-deleted', () => {
            this.isEffectDeleted = true;
        });
    },
    methods: {
        onDeleteButtonClick() {
            // DELETE at /effects/<id>
            axiosInstance.delete('/effects/' + this.effect.id)
                .then(response => {
                    emitter.emit('effect-deleted', this.effect.id);
                })
                .catch(error => {
                    console.log(error);
                });
        }
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
    align-items: end;

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

.edition-wrapper>.row>.delete-button {
    width: 10em;
    height: 2.5em;

    display: flex;
    justify-content: center;
    align-items: center;

    background-color: red;
    border-radius: 7px;
    transition-duration: 0.4s;
}

.edition-wrapper>.row>.delete-button:hover {
    background-color: #cc0000;
    cursor: pointer;
}
</style>