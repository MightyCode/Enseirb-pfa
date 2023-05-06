<template>
    <div class="wrapper">
        <div class="list-wrapper">
            <select v-model="filter">
                <option>ALL</option>
                <option>AUDIO</option>
                <option>LIGHT</option>
            </select>

            <div class="effects-list">
                <div class="effect" v-for="effect in effects" :key="effect.id" @click="selectedEffect = effect">
                    {{ effect.name }}
                </div>
            </div>

            <div class="add-effect" @click="addEffect">
                <span>+</span>
            </div>
        </div>

        <EditEffect v-if="selectedEffect !== null" :effect="selectedEffect" />
    </div>
</template>

<script>
import EditEffect from './EditEffect.vue';
import axiosInstance from '../axiosInstance';

export default {
    name: "EffectsLibrary",
    data() {
        return {
            rawEffectsList: [],
            filter: "ALL",
            selectedEffect: null
        };
    },
    mounted() {
        // GET at /effects
        axiosInstance.get('/effects')
            .then(response => {
                this.rawEffectsList = response.data;
            })
            .catch(error => {
                console.log(error);
            });
    },
    computed: {
        effects() {
            if (this.filter === "ALL") {
                return this.rawEffectsList;
            }
            else {
                return this.rawEffectsList.filter(effect => effect.type === this.filter);
            }
        }
    },
    methods: {
        /**
         * TODO: Add a new effect to the list and open the edition panel
         */
        addEffect() {
            console.log("add effect");
        }
    },
    components: { EditEffect }
}
</script>

<style scoped>
#timeline {
    width: 100%;
    height: 5em;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.wrapper {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: row;
}

.wrapper>.list-wrapper {
    width: 20%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    background-color: red;
}

.wrapper>.list-wrapper>select {
    width: 100%;
    height: 5%;

    background-color: blue;
}

.wrapper>.list-wrapper>select>option {
    width: 100%;
    height: 2em;

    background-color: green;
    text-transform: uppercase;
}

.wrapper>.list-wrapper>.effects-list {
    width: 100%;
    height: 95%;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;

    overflow-y: auto;
}

.wrapper>.list-wrapper>.effects-list>.effect {
    width: 100%;
    height: 3em;

    display: flex;
    justify-content: center;
    align-items: center;

    background-color: green;

    transition-duration: 0.4s;
    text-transform: capitalize;
}

.wrapper>.list-wrapper>.effects-list>.effect:hover {
    background-color: blue;
    cursor: pointer;
}
</style>