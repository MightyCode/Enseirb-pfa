<template>
    <header>
        <div>
            <div>
                <router-link class="tab-link" to="/new-project">Nouveau projet</router-link>
                <a class="tab-link" onclick="opentab('delete')">Supprimer projet</a>
            </div>
        </div>

        <div>
            <div class="column">
                <a class="tab-link" onclick="opentab('loadproj')">Charger projet</a>
                <router-link class="tab-link" to="/edit-project">Editer projet</router-link>
              </div>

            <div class="column">
                <a class="tab-link" onclick="opentab('vis')">Visualiser</a>
                <a class="tab-link" onclick="opentab('save')">Sauvegarder</a>
            </div>

            <div class="column">
                <a class="tab-link" onclick="opentab('editen')">Enceintes</a>
                <a class="tab-link" onclick="opentab('editlight')">Lumières</a>
            </div>

            <div class="column">
                <a class="tab-link" onclick="opentab('importer')">Importer</a>
                <a class="tab-link" onclick="opentab('export')">Exporter</a>
            </div>
        </div>

        <div>
            <div>
                <a class="tab-link" onclick="opentab('biblio')">Effets</a>
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
  width: 20%;
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
  width: 25%;
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

header>div:nth-of-type(2) {
  width: 60%;
  flex-direction: row;
}

.tab-link {
  cursor: pointer;

  background-color: #5b5b5b;
  padding: 1% 0;
  border-radius: 4px;

  transition-duration: 0.3s;
}

.tab-link:hover {
  background-color: #3b3b3b;
}
</style>