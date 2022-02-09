<template>
  <div>
    <div id="map-wrap" style="height: 100vh">
      <client-only>
        <l-map :zoom="15" :center="[45.8, 3.25]">
          <l-tile-layer
            url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
          ></l-tile-layer>
          <l-marker :lat-lng="[45.8, 3.25]"></l-marker>
        </l-map>
      </client-only>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MapPage',
  auth: false,
}
</script>
