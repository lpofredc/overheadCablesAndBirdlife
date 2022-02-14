<template>
  <div>
    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 90vh; width: 100%"
      @click="addMarker"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker
        v-for="marker in markers"
        :key="marker.id"
        :visible="marker.visible"
        :draggable="marker.draggable"
        :lat-lng.sync="marker.position"
        :icon="marker.icon"
      />
      <!-- <l-icon-default :image-path="path" /> -->
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LIconDefault } from 'vue2-leaflet'

export default {
  name: 'CustomPath',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    // LIconDefault,
  },
  data() {
    return {
      zoom: 5,
      path: '/images/',
      center: [47.41322, -1.219482],
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      markers: [],
    }
  },
  // created() {
  //   this.$nuxt.$on('resize-map', () => {
  //     console.log('retaillage')
  //   })
  // },
  methods: {
    addMarker(event) {
      const newMarker = {
        position: event.latlng,
        draggable: true,
        visible: true,
      }
      this.markers.push(newMarker)
    },
  },
}
</script>

<style scoped>
.leaflet-container {
  cursor: default !important;
}
</style>



/* Change cursor when mousing over clickable layer */
/* .leaflet-clickable {
  cursor: crosshair !important;
} */
/* Change cursor when over entire map */
