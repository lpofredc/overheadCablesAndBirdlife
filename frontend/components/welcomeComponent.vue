<template>
   <v-row dense>
          <v-col
      v-for="i in partners"
      :key="i.id"
      :loading="loading"
            cols="12"
            sm="12"
            md="6"
            lg="4"
            class="d-flex center"
          >
            <v-card

      class="mx-auto my-12"
    >
      <v-img height="100" src="https://via.placeholder.com/300.png/09f/fff"></v-img>

      <v-card-title><a :href="i.url" target="_blank">{{ i.name }}</a></v-card-title>

    </v-card>
          </v-col>
        </v-row>
    
  </div>
</template>

<script>
export default {
  name: 'WelcomeComponent',
  auth: false,
  data() {
    return {
      partners: [],
    }
  },
  mounted() {
    this.getPartners()
  },
  methods: {
    async getPartners() {
      const partners = await this.$axios.$get('custom-content/partners/')
      this.partners = partners
    },
  },
}
</script>
