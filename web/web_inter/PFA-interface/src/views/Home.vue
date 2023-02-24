<template>
        <!-- New project tab -->
        <div class="tab-content active-tab" id="newproj">
            <fieldset>
                <legend>
                    <p>Nouveau projet</p>
                    <p>Informations générales</p>
                </legend>

                <div>
                    <form>

                        <section>
                            <div class="row">
                                <label for="project-name">Nom affiché</label>
                                <input type="text" placeholder="Ex: Eirlab-Crémaillère" name="project-name">
                            </div>
    
                            <div class="row">
                                <label for="nb-lights">Nombre lumières</label>
                                <input type="number" placeholder="Ex: 54" name="nb-lights">
                            </div>
    
                            <div class="row">
                                <label for="nb-speakers">Nombre enceintes</label>
                                <input type="number" placeholder="Ex: 10" name="nb-speakers">
                            </div>
                        </section>

                        <section>
                            <div class="row">
                                <div class="col-25">
                                    <label for="myfile">Fichier audio</label>
                                </div>

                                <div class="col-75">
    
                                    <input type="file" id="actual-btn" hidden />
    
                                    <!-- our custom upload button -->
                                    <label class="btn" for="actual-btn"><i class="fa-solid fa-upload"></i></label>
    
                                    <!-- name of file chosen -->
                                    <span id="file-chosen">No file chosen</span>
                                </div>
    
                            </div>
                        </section>





                        <div class="row">
                            <input type="button" value="Submit" class="tab-link" onclick="opentab('audiovis')">
                        </div>
                    </form>
                </div>

            </fieldset>
        </div>
</template>

<script>
</script>

<style scoped>
</style>