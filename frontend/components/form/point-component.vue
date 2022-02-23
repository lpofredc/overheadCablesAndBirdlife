<template>
  <v-form class="text-center" action="test">
    <h1>{{ $t('infrstr.new_pole') }}</h1>
    <!-- <v-form ref="position"> -->
    <v-row>
      <v-col>
        <form action=""></form>
        <v-text-field
          ref="lat"
          v-model="lat"
          :label="$t('infrstr.latitude')"
          :disabled="!manual"
          type="number"
          :rules="[numberRule]"
          required
          hide-spin-buttons
        />
      </v-col>
      <v-col>
        <v-text-field
          v-model="lng"
          :label="$t('infrstr.longitude')"
          :disabled="!manual"
          type="number"
          required
          hide-spin-buttons
        />
      </v-col>
    </v-row>
    <v-row>
      <v-checkbox
        v-model="manual"
        :label="$t('infrstr.manual-hadling')"
      ></v-checkbox>
    </v-row>
    <v-select
      :items="networkOwners"
      item-text="label"
      item-value="id"
      :label="$t('infrstr.network')"
    ></v-select>

    <v-btn @click.stop="back">{{ $t('app.cancel') }}</v-btn>
  </v-form>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'PointComponent',
  data() {
    return {
      manual: false,
      numberRule: (v) => {
        if (!isNaN(parseFloat(v)) && v >= 0 && v <= 999) return true
        return 'Number has to be between 0 and 999'
      },
    }
  },
  computed: {
    lat: {
      get() {
        return this.newPoint ? this.newPoint.lat : null
      },
      set(newVal) {
        if (this.$refs.lat.validate()) {
          this.$store.commit('pointStore/add', { lat: newVal, lng: 7 })
          console.log(this.newPoint)
        }
      },
    },
    lng() {
      return this.newPoint ? this.newPoint.lng : null
    },
    ...mapGetters({
      newPoint: 'pointStore/newCoord',
      networkOwners: 'nomenclaturesStore/getOwners',
    }),
  },
  methods: {
    back() {
      this.$store.commit('pointStore/add', null)
      this.$router.back()
    },
    // updatePosition() {
    //   if (this.$refs.position.validate()) {
    //     console.log('##################################')
    //     this.$store.commit('pointStore/add', { lat: 46, lng: 7 })
    //   }
    // },
  },
}
</script>

<style>
.v-tab {
  width: 100px;
  background-color: 'indigo';
}

.v-btn {
  width: 80px;
}
</style>
