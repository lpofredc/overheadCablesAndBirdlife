<template>
  <v-snackbar v-model="display">
    ERR-{{ err.code }}: {{ err.msg }}

    <template #action="{ attrs }">
      <v-btn color="pink" text v-bind="attrs" @click="close"> Close </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  data() {
    return {
      display: false,
    }
  },
  computed: {
    ...mapGetters({
      isError: 'errorStore/isError',
      err: 'errorStore/err',
    }),
  },
  watch: {
    /**
     * Watcher: when value change (whatever true/false), that trigger display of error message
     * in snackbar by setting "diplay=true".
     */
    isError() {
      this.display = true
    },
  },
  methods: {
    /**
     * Method to close the snacbar by setting "diplay=false" and reset message content.
     * If user do not click closing button, snackbar will closed itself after a while.
     */
    close() {
      this.display = false
      this.$store.commit('errorStore/setError', { code: null, msg: null })
    },
  },
}
</script>
