<template>
  <header>
    <div>
      <div>
        <router-link class="tab-link" to="/configs">Gérer configs</router-link>
        <router-link class="tab-link" to="/projects">Gérer projets</router-link>
      </div>
    </div>

    <div>
      <div>
        <router-link class="tab-link" to="/configs/env">Environnement</router-link>
        <router-link class="tab-link" to="/edit-project">Editer projet</router-link>
      </div>
    </div>

    <div>
      <div>
        <router-link class="tab-link" to="/effects-library">Effets</router-link>
        <router-link class="tab-link" to="/vis-project">Visualiser</router-link>
      </div>
    </div>

  </header>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style scoped>
header {
  background-color: #7b7a7a;
  width: 100%;
  height: 10%;

  display: flex;
  align-items: center;
  justify-content: space-between;

  border-radius: 7px;
}

header>div {
  width: 33%;
  height: 100%;

  display: flex;
  justify-content: center;
}

header>div:first-of-type {
  border-right: #000000 1px solid;
}

header>div:last-of-type {
  border-left: #000000 1px solid;
}

header>div>div {
  height: 100%;
  width: 50%;

  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
}

header>div>.column {
  width: 50%;
  height: 100%;

  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.column>a {
  width: 75%;
  margin: 0;
}

header>div>div>a {
  width: 100%;
  text-align: center;
}

.tab-link {
  cursor: pointer;

  background-color: #5b5b5b;
  padding: 1% 0;
  border-radius: 4px;

  transition-duration: 0.3s;
  text-decoration: none;
  color: white;
}

.tab-link:visited {
  color: white;
}

.tab-link:hover {
  background-color: #3b3b3b;
}
</style>