<template>
  <v-container fluid fill-height style="background-color: yellow">
    <v-row
      class="text-center fill-height"
      fill-height
      style="background-color: blue"
    >
      <v-col cols="12" fill-height style="background-color: red">
        <v-card
          class="pa-2 overflow-auto"
          outlined
          tile
          fill-height
          style="background-color: green"
        >
          <div class="overflow-auto">
            <div v-for="i in 100" :key="i">flexbox</div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',

  data: () => ({}),
}
</script>
