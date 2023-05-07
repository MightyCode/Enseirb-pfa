<template>
    <div class="wrapper">
        <div class="list-wrapper">
            <select v-model="filter">
                <option>ALL</option>
                <option>AUDIO</option>
                <option>LIGHT</option>
            </select>

            <div class="effects-list">
                <div class="effect" v-for="effect in effects" :key="effect.id" @click="selectedEffect = effect"
                    :style="{ 'background-color': selectedEffect.id === effect.id ? '#3b3b3b' : '#5b5b5b' }">
                    {{ effect.name }}
                </div>
            </div>

            <div class="add-effect" @click="addEffect">
                <span>Nouveau</span>
            </div>
        </div>

        <EditEffect v-if="selectedEffect.id !== -1" :effect="selectedEffect" />
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
            selectedEffect: {
                id: -1
            }
        };
    },
    mounted() {
        this.refreshEffectList();
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
        addEffect() {
            // POST at /effects
            axiosInstance.post('/effects', {
                name: "Nouvel effet",
                type: "AUDIO",
                frames: []
            })
                .then(response => {
                    this.refreshEffectList();
                })
                .catch(error => {
                    console.log(error);
                });
        },
        refreshEffectList() {
            // GET at /effects
            axiosInstance.get('/effects')
                .then(response => {
                    this.rawEffectsList = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
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
}

.wrapper>.list-wrapper>select {
    width: 100%;
    height: 5%;
}

.wrapper>.list-wrapper>select>option {
    width: 100%;
    height: 2em;

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

    transition-duration: 0.4s;
    text-transform: capitalize;
}

.wrapper>.list-wrapper>.effects-list>.effect:hover {
    background-color: #3b3b3b;
    cursor: pointer;
}

.add-effect {
    width: 100%;
    background-color: #5b5b5b;
    height: 3em;

    display: flex;
    justify-content: center;
    align-items: center;
    transition-duration: 0.4s;
    border-top: 1px solid #3b3b3b;
}

.add-effect:hover {
    background-color: #3b3b3b;
    cursor: pointer;
}
</style>