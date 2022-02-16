<template>
  <div>
    <v-card>Nombre d'éléments récupérés: {{ myData.length }}</v-card>
    <div v-for="(item, index) in myData" :key="index" :value="item">
      {{ index }} - {{ item.resourcetype }} - {{ item.geometry.coordinates }}
    </div>
  </div>
</template>
<script>
import { FeatureCollection } from 'geojson'
export default {
  name: 'DataDisplay',
  props: { myData: FeatureCollection },
  data() {
    return {}
  },
}
</script>


<style>
.vuetify-logo {
  height: 180px;
  width: 180px;
  transform: rotateY(560deg);
  animation: turn 3.5s ease-out forwards 1s;
}

@keyframes turn {
  100% {
    transform: rotateY(0deg);
  }
}
</style>
