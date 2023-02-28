<template>
    <div id="main">
      <Header />
      <vue-router-view />
    </div>
</template>

<script setup>
import Header from './components/Header.vue'
</script>

<style scoped>
#main {
  width: 100%;
  height: 100%;
}
</style>
