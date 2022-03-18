<template>
  <l-map
    ref="map"
    class="d-flex align-stretch"
    :class="editMode ? 'change-map' : 'view-map'"
    :center="center"
    :bounds="bounds"
    :max-bounds="maxBounds"
    @ready="onMapReady()"
  >
    <l-tile-layer :url="url" :attribution="attribution" />
    <!-- Display of existing Pole layer-->
    <l-geo-json
      v-if="pointData"
      name="pointData"
      :geojson="pointData"
      :options-style="styleData"
      :options="GeojsonOptions"
    />
    <l-geo-json
      v-if="cablesData"
      name="lineStringData"
      :geojson="lineStringData"
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
      <v-btn fab dark small to="/supports/new" color="green">
        <v-icon>mdi-transmission-tower</v-icon>
      </v-btn>
      <v-btn fab dark small to="/lines/new" color="indigo">
        <v-icon>mdi-cable-data</v-icon>
      </v-btn>
      <v-btn fab dark small color="red">
        <v-icon>mdi-coffin</v-icon>
      </v-btn>
    </v-speed-dial>
    <!-- <l-icon-default :image-path="path" /> -->
  </l-map>
</template>

<script>
import { latLngBounds } from 'leaflet'
import { mapGetters } from 'vuex'
import '@geoman-io/leaflet-geoman-free'
import '@geoman-io/leaflet-geoman-free/dist/leaflet-geoman.css'

export default {
  name: 'DataMap',
  props: { editMode: Boolean, mode: { type: String, default: null } },

  data() {
    return {
      map: null,
      // creation markers
      createLayer: null,
      // newPoint: {
      //   type: 'Feature',
      //   properties: { id: 1, test: 'test' },
      //   geometry: null,
      //   // {
      //   //   type: 'LineString',
      //   //   coordinates: [
      //   //     [2.373047, 47.872144],
      //   //     [2.109375, 45.706179],
      //   //     [5.185547, 46.13417],
      //   //     [4.746094, 47.309034],
      //   //     [3.911133, 48.312428],
      //   //   ],
      //   // },
      // },
      // newLineMarkers: [[45, 0]],
      // Map parameters
      bounds: latLngBounds([
        [40, -6],
        [52, 10],
      ]),
      maxBounds: latLngBounds([
        [40, -6],
        [52, 10],
      ]),
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
        layer.on('pm:update', (e) => {
          console.log('featureUpdate', e)
          const newTypeObjects = {
            Line: L.Polyline,
            Point: L.Marker,
            Polygon: L.Polygon,
          }
          const newGeoObject = new newTypeObjects[e.shape](e.layer._latlngs)
          console.log('newPol', newGeoObject.toGeoJSON())
          console.log('feature', feature)
          feature.geometry = newGeoObject.toGeoJSON().geometry
        })
      }
    },
    ...mapGetters({
      cablesData: 'cablesStore/infstrDataFeatures',
      pointData: 'cablesStore/pointDataFeatures',
      lineStringData: 'cablesStore/lineDataFeatures',
      newPointCoord: 'coordinatesStore/newPointCoord',
      newLineCoord: 'coordinatesStore/newLineCoord',
    }),
  },
  watch: {
    /**
     * Watcher for "newPointCoord" value
     *
     * Only activated on "editMode=true" with "mode='point'" and if coordinate data are well
     * defined.
     * Marker position is changed based on new coordinate value.
     * If Marker does not exist, it is created with new value.
     * Map is centered on the new point.
     */
    // ##################### Works if initial point created with map control ########
    newPointCoord(newVal) {
      if (this.editMode && this.mode === 'point') {
        if (this.createLayer) {
          if (newVal && newVal.lat && newVal.lng) {
            this.createLayer.setLatLng(new L.LatLng(newVal.lat, newVal.lng))
          } else {
            // In fact, set the marker to point [0, 0]
            this.createLayer.setLatLng(new L.LatLng(null, null))
          }
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
        draggable: true,
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
    onMapReady() {
      this.map = this.$refs.map.mapObject
      // console.log('MAP', this.map)
      if (this.editMode) {
        this.map.pm.addControls({
          position: 'topleft',
          drawMarker: this.mode === 'point',
          drawCircleMarker: this.mode === 'circle-marker',
          drawPolyline: this.mode === 'line',
          drawPolygon: this.mode === 'polygon',
          drawRectangle: this.mode === 'rectangle',
          drawCircle: this.mode === 'circle',
          editMode: false,
          dragMode: false,
          removalMode: false,
          cutPolygon: false,
          rotateMode: false,
        })
        this.map.pm.setPathOptions({
          color: 'red',
          fillColor: 'red',
          fillOpacity: 0.4,
        })
        // Action on Point/Line creation
        this.map.on('pm:create', (e) => {
          this.createLayer = e.layer

          switch (this.mode) {
            case 'point':
              this.$store.commit('coordinatesStore/addPointCoord', {
                lng: e.layer.toGeoJSON().geometry.coordinates[0],
                lat: e.layer.toGeoJSON().geometry.coordinates[1],
              })
              this.map.pm.disableDraw()
              this.map.pm.addControls({
                drawMarker: false,
                dragMode: true,
                removalMode: true,
              })
              break
            case 'line':
              this.$store.commit(
                'coordinatesStore/addLineCoord',
                e.layer.toGeoJSON().geometry.coordinates
              )
              this.map.pm.addControls({
                drawPolyline: false,
                editMode: true,
                removalMode: true,
              })
              break
          }

          // Action on Point/Line change by dragging
          e.layer.on('pm:dragend', (e) => {
            switch (this.mode) {
              case 'point':
                this.$store.commit('coordinatesStore/addPointCoord', {
                  lng: e.layer.toGeoJSON().geometry.coordinates[0],
                  lat: e.layer.toGeoJSON().geometry.coordinates[1],
                })
                break
              case 'line':
                this.$store.commit(
                  'coordinatesStore/addLineCoord',
                  e.layer.toGeoJSON().geometry.coordinates
                )
                break
            }
          })

          // Action on Point/Line change by dragging
          e.layer.on('pm:edit', (e) => {
            if (this.mode === 'line')
              this.$store.commit(
                'coordinatesStore/addLineCoord',
                e.layer.toGeoJSON().geometry.coordinates
              )
          })

          // Action on Point/Line change on delete
          e.layer.on('pm:remove', (_e) => {
            switch (this.mode) {
              case 'point':
                this.$store.commit('coordinatesStore/addPointCoord', {
                  lat: null,
                  lng: null,
                })
                this.map.pm.addControls({
                  drawMarker: true,
                  dragMode: false,
                  removalMode: false,
                })
                break

              case 'line':
                this.$store.commit('coordinatesStore/addLineCoord', [])
                this.map.pm.addControls({
                  drawPolyline: true,
                  editMode: false,
                  removalMode: false,
                })
                break
            }
          })
        })
      }
    },
    // const measureControl = new window.L.Control.Measure({
    //   position: "topleft",
    //   activeColor: '#FF0000',
    //   completedColor: '#FF0000',
    //   primaryLengthUnit: "meters",
    //   secondaryLengthUnit: "kilometers",
    //   primaryAreaUnit: "sqmeters",
    //   secondaryAreaUnit: "hectares"
    // });
    // this.map.addControl(measureControl);

    // listen to events
    // this.createLayersFromJson();
    // function to check if it is a Rectangle
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
