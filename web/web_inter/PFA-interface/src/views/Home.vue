<template>
    <ImportConfig v-if="!activeConfig" />
</template>

<script>
import ImportConfig from '../components/ImportConfig.vue'

export default {
    name: 'Home',
    components: {
        ImportConfig
    },
    computed: {
        activeConfig() {
            return this.$store.state.activeConfig;
        }
    }
}
</script>

<style scoped>
</style>