<template>
    <div id="main">
      <Header />

      <div class="infobar">
        <div class="infobar-item">
          <span>Config: {{ activeConfig ? `${activeConfig.id} (${activeConfig.nbLights} lumières, ${activeConfig.nbSpeakers} enceintes)` : 'Aucun' }}</span>
        </div>

        <div class="infobar-item">
          <span>Projet: {{ activeProject ? activeProject.id : 'Aucun' }}</span>
        </div>
      </div>

      <div>
        <router-view />
      </div>
    </div>
</template>

<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header
  },
  computed: {
    activeProject() {
      return this.$store.state.activeProject;
    },

    activeConfig() {
      return this.$store.state.activeConfig;
    }
  }
}
</script>

<style scoped>
.infobar {
  height: 1.7em;
  width: 100%;

  display: flex;
}

.infobar-item {
  background-color: #7b7a7a;
  height: 100%;
  width: fit-content;
  padding: 0 1em;
  border-radius: 4px;
  margin-right: 1em;
}

#main {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

#main > div:last-of-type {
  background-color: #7b7a7a;
  height: 85%;
  border-radius: 7px;
  padding: 1%;
}
</style>
