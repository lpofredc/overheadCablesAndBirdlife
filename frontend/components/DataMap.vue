<template>
  <div>
    <l-map :zoom="zoom" :center="center" style="height: 90vh; width: 100%">
      <!--
      @click="addMarker" -->
      <l-tile-layer :url="url" :attribution="attribution" />
      
       <!-- <l-geo-json
        v-if="cablesData"
        :geojson="cablesData"
        :options-style="styleData"
        :options="GeojsonOptions"
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
        <template #activator>
          <v-btn color="primary darken-2" dark fab>
            <v-icon x-large> + </v-icon>
          </v-btn>
        </template>
        <v-btn fab dark small color="orange">
          <v-icon>mdi-shape-polygon-plus</v-icon>
        </v-btn>
        <v-btn fab dark small color="green">
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
import { FeatureCollection } from 'geojson'
import { LCircleMarker } from 'vue2-leaflet'

export default {
  name: 'DataMap',
  props: { cablesData: FeatureCollection },

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
  computed: {
    
    GeojsonOptions() {
      return {
        onEachFeature: this.GeoJsonOnEachFeature,
        pointToLayer: this.GeoJsonPointToLayer
      }
    },
    GeoJsonOnEachFeature() {
      return (feature, layer) => {
        layer.bindPopup(`ma <strong>bindPopup</strong> pour<br>${feature.geometry.type} avec  id =>${feature.properties.id}`)
      }
    },
    pointData() {
      const geoJson = {type:'FeatureCollection',features:this.cablesData.filter((e) => e.geometry.type === 'Point')}
      console.log('pointData', geoJson)
      return geoJson
    },
    lineStringData() {
      const geoJson = {type:'FeatureCollection',features:this.cablesData.filter((e) => e.geometry.type === 'LineString')}
      console.log('lineStringData', geoJson)
      return geoJson
    }
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
        console.log('############################################### ')
        return LCircleMarker(latlng, {
          radius: 10,
          fillOpacity: 0.85,
        })
      }
    },
    GeoJsonPointToLayer(feature, latlng) {
        return L.circleMarker(latlng, {
    radius: 8,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
});
    
      }
  ,
    styleData(feature) {
      // const weight = 0.5
      // const linecolor = 'red'
      // const opacity = 0.8
      // function (feature: Feature) {
      console.log(feature.geometry.type + ' id => ' + feature.properties.id)
      if (feature.geometry.type === 'LineString') {
        return {
          color: 'green',
          // weight,
          // opacity,
          // dashArray: '',
          // lineCap: 'butt',
          // lineJoin: 'miter',
          // fillColor: 'rgba(0,0,0,0)',
          // fillOpacity: '0.0',
          // }
        }
      } else {
        return {
          color: 'red',
        }
      }
    },
  }
  //   addMarker(event) {
  //     const newMarker = {
  //       position: event.latlng,
  //       draggable: true,
  //       visible: true,
  //     }
  //     this.markers.push(newMarker)
  //   },
}
</script>

<style scoped>
.fab {
  z-index: 10000;
}
</style>
