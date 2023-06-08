<template>
  <l-map ref="map" class="d-flex align-stretch" :useGlobalLeaflet="false" :zoom="zoom" :center="center" @ready="mapReady">
    <l-tile-layer v-for="baseLayer in baseLayers" :key="baseLayer.id" :name="baseLayer.name" :url="baseLayer.url"
      :visible="baseLayer.default" :attribution="baseLayer.attribution" layer-type="base" />
    <l-control-layers />
    <l-geo-json :geojson="pointData" :options="geojsonOptions" />
    <l-geo-json :geojson="lineStringData" :options="geojsonOptions" />
    <utils-map-actions-menu v-if="!editMode" />
  </l-map>
</template>

<script setup lang="ts">
import { LMap, LTileLayer, LGeoJson, LControlLayers } from "@vue-leaflet/vue-leaflet";
import { useMapLayersStore } from "~/store/mapLayersStore"
import { GeoJSON, Feature } from "geojson"
import { useCablesStore } from "~/store/cablesStore"
import { StoreGeneric } from "pinia"
// import L from "leaflet"
// import '@geoman-io/leaflet-geoman-free'
import '@geoman-io/leaflet-geoman-free/dist/leaflet-geoman.css'

// if (!map.pm) {
//   await import(/* webpackChunkName: "leaflet-geoman" */ '@geoman-io/leaflet-geoman-free');
//   L.PM.reInitLayer(map)
// }

const props = defineProps({ editMode: Boolean, mode: { type: String, default: null } })

const map = ref()
const cableStore : StoreGeneric  = useCablesStore()
const mapLayersStore : StoreGeneric = useMapLayersStore()
const zoom : Ref<number> = ref<number>(6);
const center : Ref<number[]>= ref<number[]>([46.6423682169416,2.1940236627886227]);
const pointData: ComputedRef<GeoJSON> = computed<GeoJSON>(() => cableStore.getPointDataFeatures);
const lineStringData: ComputedRef<GeoJSON> = computed<GeoJSON>(() => cableStore.getLineDataFeatures);
const baseLayers = computed(() => {
    return mapLayersStore.baseLayers
})



const onEachFeature = (feature : Feature, layer : any) => {
    // TODO To be adapted
    layer.bindPopup(
      `ma <strong>bindPopup</strong> pour<br>${feature.geometry.type} avec  id =>${feature.properties?.id}`
    )
    // remove pm from layer to prevent action from geoman (no more drag/edit/remove ...)
    delete layer.pm
    layer.setStyle({ pmIgnore: false })
  }

const pointToLayer = async (_feature: Feature, latlng : any ) => {
    const { circleMarker } = await import("leaflet/dist/leaflet-src.esm");
    return circleMarker(latlng, {
        radius: 5,
        fillColor: '#ff7800',
        color: '#000',
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8,
        // draggable: true,
      })}
      // return L.circleMarker(latlng, {
      //   radius: 5,
      //   fillColor: '#ff7800',
      //   color: '#000',
      //   weight: 1,
      //   opacity: 1,
      //   fillOpacity: 0.8,
      //   // draggable: true,
      // })
    const geojsonOptions = {
        onEachFeature,
        pointToLayer
      }
    const mapReady = async () => {
      const { circleMarker } = await import("leaflet/dist/leaflet-src.esm");
      window.L = map.value.leafletObject;
      await import("@geoman-io/leaflet-geoman-free");
      // console.log('L Object', window.L);
      // window.L.pm.addControls({
      //   position: "topleft",
      //   drawCircle: false,
      // });
    };
// onMounted(() => {
//     if (!process.server) {
//         console.log(`MAP`, map)
//   }
// })

</script>

<style></style>
