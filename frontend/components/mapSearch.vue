<template>
  <l-map id="map" ref="map" class="d-flex" :zoom="zoom" :center="center" @ready="hookUpDraw">
    <!-- <l-map id="map" ref="map" class="d-flex align-stretch" :zoom="zoom" :center="center" @ready="hookUpDraw"> -->
    <template v-if="mapReady">
      <l-tile-layer v-if="mapReady" v-for="baseLayer in baseLayers" :key="baseLayer.id" :name="baseLayer.name"
        :url="baseLayer.url" :visible="baseLayer.default" :attribution="baseLayer.attribution" layer-type="base" />
      <l-control-layers />
      <l-geo-json v-if="pointData" :geojson="pointData" :options="geojsonOptions" />
      <l-geo-json :geojson="lineStringData" :options="geojsonOptions" />
    </template>
    <utils-map-actions-menu v-if="!editMode" />
  </l-map>
</template>

<script setup lang="ts">
import "leaflet";
import { circleMarker } from "leaflet";
import { LMap, LTileLayer, LGeoJson, LControlLayers } from "@vue-leaflet/vue-leaflet";
// import { useMapLayersStore } from "store/mapLayersStore";
import { GeoJSON, Feature } from "geojson"
// import { useCablesStore } from "~/store/cablesStore"
import { StoreGeneric } from "pinia"
import type {Map, PointTuple, GeoJSONOptions, Layer} from "leaflet";

await import("@geoman-io/leaflet-geoman-free");

const {editMode, mode} = defineProps({ editMode: Boolean, mode: { type: String, default: null } })

const map = ref()

const mapObject : Ref<null | Map> = ref(null)
const createLayer: Ref<Layer |null> = ref(null)
const mapReady : Ref<Boolean> = ref(false)
const cableStore : StoreGeneric  = useCablesStore()
const mapLayersStore : StoreGeneric = useMapLayersStore()
const coordinatesStore : StoreGeneric = useCoordinatesStore()
const zoom : Ref<number> = ref<number>(6);
const center : Ref<PointTuple>= ref([46.6423682169416,2.1940236627886227] as PointTuple);
const pointData: ComputedRef<GeoJSON> = computed<GeoJSON>(() => cableStore.getPointDataFeatures);
const lineStringData: ComputedRef<GeoJSON> = computed<GeoJSON>(() => cableStore.getLineDataFeatures);

const baseLayers = computed(() => mapLayersStore.baseLayers)

const newPointCoord = computed(() => coordinatesStore.newPointCoord)
const newLineCoord = computed(() => coordinatesStore.newLineCoord)

const onEachFeature = (feature : Feature, layer : any) => {
  // TODO To be adapted
  layer.bindPopup(
    `ma <strong>bindPopup</strong> pour<br>${feature.geometry.type} avec  id =>${feature.properties?.id}`
  )
  // remove pm from layer to prevent action from geoman (no more drag/edit/remove ...)
  console.log('layer', layer)
  // delete layer.pm
  // layer.setStyle({ pmIgnore: false })
}

const geojsonOptions : GeoJSONOptions = reactive({
  onEachFeature,
})


const hookUpDraw = async () => {
  mapObject.value = map.value?.leafletObject;
  mapReady.value = true;
  console.log("mapObject", mapObject.value);

  if (mapObject.value && editMode) {
    // mapObject.value.pm.setLang("en_gb");
    mapObject.value.pm.addControls({
      position: 'topleft',
          drawMarker: mode === 'point',
          drawCircleMarker: mode === 'circle-marker',
          drawPolyline: mode === 'line',
          drawPolygon: mode === 'polygon',
          drawRectangle: mode === 'rectangle',
          drawCircle: mode === 'circle',
          drawText: false,
          editMode: false,
          dragMode: false,
          removalMode: false,
          cutPolygon: false,
          rotateMode: false,
    });
    mapObject.value.pm.setPathOptions({
          color: 'red',
          fillColor: 'red',
          fillOpacity: 0.4,
        })
    mapObject.value.on('pm:create', (e) => {
          createLayer.value = e.layer
          switch (mode) {
            case 'point':
              console.log('createLayer', createLayer.value.toGeoJSON())
              if (createLayer.value.toGeoJSON()) {
              coordinatesStore.setNewGeoJSONPoint(
                createLayer.value.toGeoJSON().geometry
              )
              mapObject.value?.pm.disableDraw()
              mapObject.value?.pm.addControls({
                drawMarker: false,
                dragMode: true,
                removalMode: true,
              })}
              break
            case 'line':
              coordinatesStore.newLineCoord = createLayer.value.toGeoJSON().geometry.coordinates
              mapObject.value?.pm.addControls({
                drawPolyline: false,
                editMode: true,
                removalMode: true,
              })
              break
          }
          // // set listener on drag event on this layer
          // this.handleDrag(createLayer)

          // // in case of remove event, trigger handleRemove() method
          // e.layer.on('pm:remove', (_e) => {
          //   this.handleRemove()
          // })
        })
    // mapObject.value.on("pm:drawstart", ({ workingLayer, shape }) => {
    //   console.log('drawstart', workingLayer)
    //   workingLayer.on("pm:vertexadded", (e) => {
    //     console.log('vertexadded', e, shape);
    //     geofence.value.push(e)
    //   });
    // });

    // mapObject.value.on("pm:drawend", () => {
    //   console.log("drawend", geofence.value);
    // });
  }
};


onBeforeMount(async () => {
  // const { circleMarker } = await import("leaflet/dist/leaflet-src.esm");
  geojsonOptions.pointToLayer = (_feature: Feature, latlng : any ) => {
  return circleMarker(latlng, {
    radius: 5,
    fillColor: '#ff7800',
    color: '#000',
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8,
    // draggable: true,
  })}
})

</script>

<style>
#map {
  width: 100%;
}
</style>
