<template>
  v
  <l-map ref="map" class="d-flex align-stretch" :useGlobalLeaflet="false" :zoom="zoom" :center="center"
    @ready="hookUpDraw">
    <template v-if="mapReady">
      <l-tile-layer v-if="mapReady" v-for="baseLayer in baseLayers" :key="baseLayer.id" :name="baseLayer.name"
        :url="baseLayer.url" :visible="baseLayer.default" :attribution="baseLayer.attribution" layer-type="base" />
      <l-control-layers />
      <l-geo-json :geojson="pointData" :options="geojsonOptions" />
      <l-geo-json :geojson="lineStringData" :options="geojsonOptions" />
    </template>
    <utils-map-actions-menu v-if="!editMode" />
  </l-map>
</template>

<script setup lang="ts">
import "leaflet";
import { LMap, LTileLayer, LGeoJson, LControlLayers } from "@vue-leaflet/vue-leaflet";
import { useMapLayersStore } from "~/store/mapLayersStore"
import { GeoJSON, Feature } from "geojson"
import { useCablesStore } from "~/store/cablesStore"
import { StoreGeneric } from "pinia"
import type {Map, PointTuple, GeoJSONOptions} from "leaflet";
// import "@geoman-io/leaflet-geoman-free";
// import "@geoman-io/leaflet-geoman-free/dist/leaflet-geoman.css";
// await import("@geoman-io/leaflet-geoman-free");

const props = defineProps({ editMode: Boolean, mode: { type: String, default: null } })

const map = ref()
const mapObject : Ref<null | Map> = ref(null)
const mapReady : Ref<Boolean> = ref(false)
const cableStore : StoreGeneric  = useCablesStore()
const mapLayersStore : StoreGeneric = useMapLayersStore()
const zoom : Ref<number> = ref<number>(6);
const center : Ref<PointTuple>= ref([46.6423682169416,2.1940236627886227] as PointTuple);
const pointData: ComputedRef<GeoJSON> = computed<GeoJSON>(() => cableStore.getPointDataFeatures);
const lineStringData: ComputedRef<GeoJSON> = computed<GeoJSON>(() => cableStore.getLineDataFeatures);

const baseLayers = computed(() => {
    console.log('mapLayersStore.baseLayer', mapLayersStore.baseLayer)
    return mapLayersStore.baseLayers
})

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

    // const mapReady = async () => {
    //   window.L = map.value.leafletObject;
    //   // await import("@geoman-io/leaflet-geoman-free");
    //   // // console.log('L Object', window.L);
    //   // window.L.pm.addControls({
    //   //   position: "topleft",
    //   //   drawCircle: false,
    //   // });
    // };

    const hookUpDraw = async () => {
      if (!map.pm) {

  await import(/* webpackChunkName: "leaflet-geoman" */ '@geoman-io/leaflet-geoman-free');
  mapObject.value = map.value.leafletObject;
  mapObject.PM.reInitLayer(map)
}
      // console.log('0')
      // console.log('PROCESS', process)
      // if (process.client) {

      //   console.log('MAP', map);
      //   console.log('L', L);
      //   // if (!map.pm) {
      //   //  await import("@geoman-io/leaflet-geoman-free");
      //   // }
      //   mapObject.value = map.value.leafletObject;
      //   mapReady.value = true;
      //   console.log('mapObject', mapObject.value)
      // }
      // await import("@geoman-io/leaflet-geoman-free");
//       if (!map.pm) {
//         await import("@geoman-io/leaflet-geoman-free");
//   L.PM.reInitLayer(map)
// }
      // console.log('MAP', map);
      // mapObject.value = map.value.leafletObject;
      // mapReady.value = true;
      // console.log('mapObject', mapObject.value)
      // mapObject.value.pm.setLang("en_gb");
      // mapObject.value.pm.addControls({
      //   position: "topleft",
      //   drawCircle: true,
      // });
      // mapObject.value.on("pm:drawstart", ({ workingLayer }) => {
      //   workingLayer.on("pm:vertexadded", (e) => {
      //     console.log(e);
      //     // geofence.value.push(e);
      //   });
      // });
      // mapObject.value.on("pm:drawend", () => {
      //   console.log('geofence');
      // });
    };

  onBeforeMount(async () => {
    const { circleMarker } = await import("leaflet/dist/leaflet-src.esm");
    geojsonOptions.pointToLayer = (_feature: Feature, latlng : any ) => {
    return circleMarker(latlng, {
        radius: 5,
        fillColor: '#ff7800',
        color: '#000',
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8,
        draggable: true,
      })}
  })

</script>

<style></style>
