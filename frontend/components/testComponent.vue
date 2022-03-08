<template>
  <div style="display: none">
    <slot v-if="ready"></slot>
  </div>
</template>

<script>
/**
 * Geoman for Vue - created by Max Kalus
 *
 * Install using:
 * npm i @geoman-io/leaflet-geoman-free uuid
 */
import '@geoman-io/leaflet-geoman-free'
import '@geoman-io/leaflet-geoman-free/dist/leaflet-geoman.css'
// import L from 'leaflet'
// import { v4 as uuidv4 } from 'uuid'

export default {
  name: 'TestComponent',
  props: {
    map: {
      type: Object,
      required: true,
    },
    geoJson: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    ready: true,
  }),
  created() {
    if (this.map) {
      console.log('création')
      console.log(this.map)
      console.log(this.map.pm)
      // set global options
      this.map.pm.setGlobalOptions({ allowSelfIntersection: false })
      // add controls
      this.map.pm.addControls({
        position: 'topleft',
      })
      // listen to events
      this.map.on('pm:create', this.mapUpdated)
      this.map.on('pm:remove', this.mapUpdated)
      this.map.on('pm:cut', this.mapUpdated)
      // add initial data
      this.importGeoJSON(this.geoJson)
    }
  },
  methods: {
    mapUpdated(event) {
      // add listeners on creation and delete on removal
      if (event.type === 'pm:create') {
        event.layer.on('pm:edit', this.mapUpdated)
        // add data
        event.layer.properties = {
          shape: event.shape,
        }
        // radius for circles
        if (event.shape === 'Circle') {
          event.layer.properties.radius = event.layer.getRadius()
        }
        event.layer.internalId = uuidv4()
      }
      if (event.type === 'pm:remove') {
        event.layer.off() // remove all event listeners
      }
      // emit event
      this.$emit('change', this.getDataAsGeoJSON())
    },
    // // export data as GeoJSON object
    // getDataAsGeoJSON() {
    //   // create FeatureCollection
    //   const geoJSON = {
    //     type: 'FeatureCollection',
    //     features: [],
    //   }
    //   // export each layer
    //   this.map.eachLayer(function (layer) {
    //     if (
    //       layer.internalId &&
    //       (layer instanceof L.Path || layer instanceof L.Marker)
    //     ) {
    //       const geoJSONShape = layer.toGeoJSON(16) // to precise geo shape!
    //       geoJSONShape.properties = layer.properties
    //       geoJSONShape.id = layer.internalId
    //       geoJSON.features.push(geoJSONShape)
    //       // normalize coordinates (> 180/>90)
    //       // TODO
    //     }
    //   })
    //   return geoJSON
    // },
    // // inport data from GeoJSON
    // importGeoJSON(geoJSON) {
    //   if (
    //     geoJSON &&
    //     geoJSON.type === 'FeatureCollection' &&
    //     geoJSON.features &&
    //     geoJSON.features.length
    //   ) {
    //     geoJSON.features.forEach((feature) => {
    //       const shape = feature.properties && feature.properties.shape
    //       const coordinates = feature.geometry && feature.geometry.coordinates
    //       let layer // define shape for later use
    //       switch (shape) {
    //         case 'Circle':
    //           layer = new LCircle(
    //             [coordinates[1], coordinates[0]],
    //             feature.properties.radius
    //           )
    //           break
    //         case 'CircleMarker':
    //           layer = new L.CircleMarker([coordinates[1], coordinates[0]])
    //           break
    //         case 'Marker':
    //           layer = new L.Marker([coordinates[1], coordinates[0]])
    //           break
    //         case 'Polyline':
    //           layer = new L.Polyline(this.switchCoordinates(coordinates))
    //           break
    //         case 'Polygon':
    //           layer = new L.Polygon(this.switchCoordinates(coordinates))
    //           break
    //         case 'Rectangle':
    //           layer = new L.Rectangle(this.switchCoordinates(coordinates))
    //           break
    //       }
    //       if (layer) {
    //         layer.addTo(this.map)
    //         layer.internalId = feature.id
    //         layer.properties = feature.properties
    //         // add event listener
    //         layer.on('pm:edit', this.mapUpdated)
    //       }
    //     })
    //   }
    // },
    // // switch coordinates -> geoJSON to Leaflet
    // switchCoordinates(coordinates) {
    //   return [coordinates[0].map((pair) => [pair[1], pair[0]])]
    // },
  },
}
</script>
