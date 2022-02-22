<template>
  <div>
    <l-map
      :class="editMode ? 'change-map' : 'view-map'"
      :zoom="zoom"
      :center="center"
      style="height: 90vh; width: 100%"
      @click="addMarker"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
      <!-- <l-marker
        v-for="marker in markers"
        :key="marker.id"
        :visible="marker.visible"
        :draggable="marker.draggable"
        :lat-lng.sync="marker.position"
        :icon="marker.icon"
      /> -->
      <l-marker
        v-if="newMarker"
        :lat-lng.sync="newMarker.position"
        :draggable="true"
        @dragend="updatePosition"
      />
      <l-geo-json
        v-if="cablesData"
        :geojson="lineStringData"
        :options-style="styleData"
        :options="GeojsonOptions"
      />
      <l-geo-json
        v-if="cablesData"
        :geojson="pointData"
        :options-style="styleData"
        :options="GeojsonOptions"
      />

      <v-speed-dial
        class="fab mb-5"
        absolute
        bottom
        right
        direction="top"
        transition="slide - y - reverse - transition"
      >
        <template v-if="!editMode" #activator>
          <v-btn color="primary darken-2" dark fab>
            <v-icon x-large> + </v-icon>
          </v-btn>
        </template>
        <v-btn fab dark small color="orange">
          <v-icon>mdi-shape-polygon-plus</v-icon>
        </v-btn>
        <v-btn fab dark small color="green" @click.stop="createPoint">
          <v-icon>mdi-transmission-tower</v-icon>
        </v-btn>
        <v-btn fab dark small color="indigo">
          <v-icon>mdi-cable-data</v-icon>
        </v-btn>
        <v-btn fab dark small color="red">
          <v-icon>mdi-coffin</v-icon>
        </v-btn>
      </v-speed-dial>
      <l-icon-default :image-path="path" />
    </l-map>
  </div>
</template>

<script>
// import { FeatureCollection } from 'geojson'
import { mapGetters } from 'vuex'

export default {
  name: 'DataMap',
  props: { editMode: Boolean },

  data() {
    return {
      newMarker: null,
      zoom: 5,
      path: '/images/',
      center: [47.41322, -1.219482],
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    }
  },
  computed: {
    // Map property options to matching function
    GeojsonOptions() {
      return {
        onEachFeature: this.GeoJsonOnEachFeature,
        pointToLayer: this.GeoJsonPointToLayer,
      }
    },
    // Define code executed for each Feature
    GeoJsonOnEachFeature() {
      return (feature, layer) => {
        // TODO To be adapted
        layer.bindPopup(
          `ma <strong>bindPopup</strong> pour<br>${feature.geometry.type} avec  id =>${feature.properties.id}`
        )
      }
    },
    // pointData() {
    //   const geoJson = {
    //     type: 'FeatureCollection',
    //     features: this.PointData,
    //   }
    //   return geoJson
    // },
    // lineStringData() {
    //   const geoJson = {
    //     type: 'FeatureCollection',
    //     features: this.cablesData.filter(
    //       (e) => e.geometry.type === 'LineString'
    //     ),
    //   }
    //   return geoJson
    // },
    // pointData() {
    //   const geoJson = {
    //     type: 'FeatureCollection',
    //     features: this.cablesData.filter((e) => e.geometry.type === 'Point'),
    //   }
    //   return geoJson
    // },
    // lineStringData() {
    //   const geoJson = {
    //     type: 'FeatureCollection',
    //     features: this.cablesData.filter(
    //       (e) => e.geometry.type === 'LineString'
    //     ),
    //   }
    //   return geoJson
    // },
    ...mapGetters({
      cablesData: 'cablesStore/infstrDataFeatures',
      pointData: 'cablesStore/pointDataFeatures',
      lineStringData: 'cablesStore/lineDataFeatures',
      newCoord: 'pointStore/newMarker',
    }),
  },
  methods: {
    // INFO: Passé en computed, onEachFeature devient alors un object
    // (j'avais un message comme quoi le props options attendait un obkjet et non une function)
    // C'est aussi le cas ici: https://vue2-leaflet.netlify.app/examples/geo-json.html
    // onEachFeature(_feature, layer) {
    //   layer.bindPopup('coucou', _feature)
    // },
    changePointMarker(_feature, latlng) {
      if (feature.geometry.type === 'Point') {
        return LCircleMarker(latlng, {
          radius: 2,
          fillOpacity: 0.85,
        })
      }
    },
    GeoJsonPointToLayer(_feature, latlng) {
      return L.circleMarker(latlng, {
        radius: 5,
        fillColor: '#ff7800',
        color: '#000',
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8,
      })
    },
    styleData(feature) {
      // const weight = 0.5
      // const linecolor = 'red'
      // const opacity = 0.8
      // function (feature: Feature) {
      if (feature.geometry.type === 'LineString') {
        return {
          color: 'green',
          // weight,
          // opacity,
          // dashArray: '',
          // lineCap: 'butt',
          // lineJoin: 'miter',
          // fillColor: 'rgba(0,0,0,0)',
          // fillOpacity: '0.0',green
          // }
        }
      } else {
        return {
          color: 'red',
        }
      }
    },
    createPoint() {
      this.$router.push('/point')
    },
    addMarker(event) {
      if (this.editMode) {
        this.newMarker = {
          position: event.latlng,
          draggable: true,
          visible: true,
        }
        this.$store.commit('pointStore/add', this.newMarker.position)
      }
    },
    updatePosition() {
      if (this.editMode) {
        this.$store.commit('pointStore/add', this.newMarker.position)
      }
    },
  },
}
</script>

<style scoped>
.fab {
  z-index: 10000;
}

.view-map {
  cursor: grab;
}

.change-map {
  cursor: crosshair;
}
</style>
