// Nuxt Store module: cablesStore for Cables module
import { defineStore } from 'pinia'

export const useCablesStore = defineStore('cables', {
  state: () => ({
    infstrData: {}, // Infrastructure data
    // pointData: {}, // Pole and Pylon data
    // lineData: {}, // Cable lines data
    opData: [],
    pointOpData: [],
    lineOpData: []
  }),
  getters: {
    // // get FeatureCollection data
    // infstrData(state) {
    //   return state.infstrData
    // },
    // get FeatureCollection array containing data (Json Object)
    getInfstrDatafeatures(state) {
      return state.infstrData.features
    },
    // pointData(state) {
    //   return state.pointData
    // },
    getPointDataFeatures(state) {
      return state.infstrData.features?.filter(
        elem => elem.resourcetype === 'Point'
      )
    },
    // lineData(state) {
    //   return state.lineData
    // },
    getLineDataFeatures(state) {
      return state.infstrData.features?.filter(
        elem => elem.resourcetype === 'Line'
      )
    },
    getOpData(state) {
      return state.opData
    },
    getPointOpData(state) {
      return state.pointOpData
    },
    getLineOpData(state) {
      return state.lineOpData
    }
  },
  actions: {
    async getInfrstrData(filter) {
      await $fetch('/api/v1/cables/infrastructures', filter).then((data) => {
        this.infstrData = data
        console.log('DATA', this.infstrData, data)
      }).catch((error) => { console.error(error) })

      // gather Point and Line from fetched infrastructure data
      // filter Point objects in data.features and set filtered array to "state.pointData.features"
      // this.pointData.features = dataCopy.features?.filter(
      //   elem => elem.resourcetype === 'Point'
      // )
      // // filter Line objects in data.features and set filtered array to "state.lineData.features"
      // this.lineData.features = dataCopy.features?.filter(
      //   elem => elem.resourcetype === 'Line'
      // )
    },
    setInfrstrData(data) {
      this.infstrData = data
    },
    addOperation(data) {
      this.opData = data.all
      this.pointOpData = data.point
      this.lineOpData = data.line
    }
  }
})
