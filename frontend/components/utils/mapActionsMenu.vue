<template>
    <div class="d-flex align-end float-right ma-5">
        <v-menu transition="fade-transition">
            <template v-if="!$parent.editMode" v-slot:activator="{ props }">
                <v-btn id="speedDial" dark color="primary" icon="mdi-plus" v-bind="props" class="float-right" />
            </template>
            <v-btn fab dark class="ma-1" icon="mdi-shape-polygon-plus" size="small" color="orange" />
            <v-btn fab dark class="ma-1" icon="mdi-transmission-tower" size="small" to="/supports/new" color="green" />
            <v-btn fab dark class="ma-1" icon="mdi-cable-data" size="small" to="/lines/new" color="indigo" />
            <v-btn fab dark class="ma-1" icon="mdi-coffin" size="small" to="/mortality/new" color="red" />
        </v-menu>
    </div>
</template>

<script setup>


</script>
<style>
#speedDial {
    z-index: 10000;
}
</style>
