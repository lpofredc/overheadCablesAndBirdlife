<template>
  <div>
    <multipane
      v-if="$vuetify.breakpoint.lgAndUp"
      class="custom-resizer"
      layout="vertical"
    >
      <!--
      @paneResize="$nuxt.$emit('resize-map')" -->
      <div
        class="pane"
        :style="{ minWidth: '10%', width: '50%', maxWidth: '90%' }"
      >
        <Map />
      </div>
      <multipane-resizer></multipane-resizer>
      <div class="pane" :style="{ flexGrow: 1 }">
        <DataDisplay />
      </div>
    </multipane>
    <v-tabs
      v-if="$vuetify.breakpoint.mdAndDown"
      fixed-tabs
      background-color="indigo"
      dark
    >
      <v-tab> Map </v-tab>
      <v-tab-item> <Map /> </v-tab-item>
      <v-tab> DataDisplay </v-tab>
      <v-tab-item> <DataDisplay /> </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
import { Multipane, MultipaneResizer } from 'vue-multipane'
export default {
  name: 'MainPage',
  auth: false,
  components: {
    Multipane,
    MultipaneResizer,
  },
  data() {
    return {
      app_name: 'Overhead Cables & BirdLife',
      drawer_opened: true, // drawer closed by default
      miniVariant: true, // wide drawer when opening by default
    }
  },
  methods: {
    openDrawer() {
      return this.$auth.loggedIn ? this.drawer_opened : false
    },
  },
}
</script>

<style  lang="scss">
.vert.custom-resizer {
  width: 100%;
  height: 100%;
}

.custom-resizer > .pane {
  text-align: left;
  padding: 15px;
  overflow: hidden;
  background: #eee;
  border: 1px solid #ccc;
}

.custom-resizer > .multipane-resizer {
  height: 100vh;
  margin: 0;
  left: 0;
  position: relative;

  &:before {
    display: block;
    content: '';
    width: 3px;
    height: 40px;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -20px;
    margin-left: -1.5px;
    border-left: 1px solid #ccc;
    border-right: 1px solid #ccc;
  }

  &:hover {
    &:before {
      border-left: 1px solid blue;
      border-right: 1px solid blue;
    }
  }
}
</style>
detect size change
