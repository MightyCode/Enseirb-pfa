<template>
    <div class="wrapper">
        <div class="list-wrapper">
            <select v-model="filter">
                <option>ALL</option>
                <option>AUDIO</option>
                <option>LIGHT</option>
            </select>

            <div class="effects-list">
                <div class="effect" v-for="effect in effects" :key="effect.id">
                    {{ effect.name }}
                </div>
            </div>

            <div class="add-effect" @click="addEffect">
                <span>+</span>
            </div>
        </div>

        <div class="selected-effect" v-if="selectedEffect">
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
                    <select name="effect-type" id="effect-type">
                        <option>AUDIO</option>
                        <option>LIGHT</option>
                    </select>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "EffectsLibrary",
    data() {
        return {
            rawEffectsList: [{ id: 0, name: "test", type: "audio" }, { id: 1, name: "test2", type: "light" }],
            filter: "ALL",
            selectedEffect: true
        };
    },
    computed: {
        effects() {
            if (this.filter.toLowerCase() === 'all') {
                return this.rawEffectsList;
            } else {
                return this.rawEffectsList.filter(effect => effect.type === this.filter.toLowerCase());
            }
        }
    },
    methods: {
        /**
         * TODO: Add a new effect to the list and open the edition panel
         */
        addEffect() {
            console.log('add effect');
        }
    }
}
</script>

<style scoped>
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

.wrapper>.selected-effect {
    width: 80%;
    height: 100%;

    display: flex;
    flex-direction: column;

    padding: 1em 2em;
}

.wrapper>.selected-effect>.row {
    width: 100%;

    display: flex;
    flex-direction: row;
    align-items: center;
}

.wrapper>.selected-effect>.row>span {
    font-size: 1.5em;
    font-weight: bold;
}


.wrapper>.selected-effect>.row>div {
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;

    margin: 0 1em;
}

.wrapper>.selected-effect>.row>div:first-of-type {
    margin-left: 0;
}

.wrapper>.selected-effect>.row>div:last-of-type {
    margin-right: 0;
}

.wrapper>.selected-effect>.row>div>input,
.wrapper>.selected-effect>.row>div>select {
    width: 30em;
    height: 3em;

    padding: 0 1em;
    border-radius: 7px;

    border: 0;
}

.wrapper>.selected-effect>.row>div>input:focus,
.wrapper>.selected-effect>.row>div>select:focus {
    outline: none;
    border: 0;
}
</style>