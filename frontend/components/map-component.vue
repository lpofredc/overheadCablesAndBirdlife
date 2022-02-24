<template>
  <div>
    <l-map
      :class="editMode ? 'change-map' : 'view-map'"
      :center="center"
      :bounds="bounds"
      :max-bounds="maxBounds"
      style="height: 90vh; width: 100%"
      @click="recordPosition"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
      <!-- l-marker Not visible if lat or lng data is null -->
      <l-marker
        v-if="newMarker"
        :lat-lng.sync="newMarker.position"
        :draggable="true"
        :max-bounds="maxBounds"
        :visible="newCoord.lat !== null && newCoord.lng !== null"
        @dragend="updatePosition"
      />
      <!-- <l-marker
        v-for="marker in markers"
        :key="marker.id"
        :visible="marker.visible"
        :draggable="marker.draggable"
        :lat-lng.sync="marker.position"
        :icon="marker.icon"
      /> -->
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
    ##{{ newCoord }}##
  </div>
</template>

<script>
import { latLngBounds } from 'leaflet'
import { mapGetters } from 'vuex'

export default {
  name: 'DataMap',
  props: { editMode: Boolean },

  data() {
    return {
      bounds: latLngBounds([
        [40, -6],
        [52, 10],
      ]),
      maxBounds: latLngBounds([
        [40, -6],
        [52, 10],
      ]),
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
      newCoord: 'pointStore/newCoord',
      newLat: 'pointStore/newLat',
    }),
  },
  watch: {
    /**
     * Watcher for "newCoord" value
     *
     * Only activated on "editMode" and if coordinate data are well defined.
     * Marker position is changed based on new coordinate value.
     * If Marker does not exist, it is created with new value.
     * Map is centered on the new point.
     */
    newCoord(newVal) {
      if (this.editMode) {
        if (newVal && newVal.lat && newVal.lng) {
          if (this.newMarker) {
            // if Marker already exists
            this.newMarker.position = newVal
          } else {
            // else create it and set values
            this.newMarker = {
              position: newVal,
              draggable: true,
            }
          }
          // map center on marker
          this.center = [newVal.lat, newVal.lng]
        }
      }
    },
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
    /**
     * Method that records pointer position on the map
     *
     * Only activated on "editMode"
     * The position is recorded in store value "newCoord". A wtacher on newCoord will the create
     * or move the Marker as needed on the map.
     */
    recordPosition(event) {
      if (this.editMode) {
        this.$store.commit('pointStore/add', event.latlng)
      }
    },
    /**
     * Method that records pointer position when moved on the map (linked to @drag)
     *
     * Only activated on "editMode"
     * The position is recorded in store value "newCoord". A wtacher on newCoord will the create
     * or move the Marker as needed on the map.
     */
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
