<template>
    <div id="main">
      <Header />
      <div>
        <router-view />
      </div>
    </div>
</template>

<script setup>
import Header from './components/Header.vue'
</script>

<style scoped>
#main {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

#main > div {
  background-color: #7b7a7a;
  height: 88%;
  border-radius: 7px;
  padding: 1%;
}
</style>
