<template>
  <v-container fluid fill-height style="background-color: yellow">
    <v-row class="text-center fill-height" fill-height style="background-color: blue">
      <v-col cols="12" fill-height style="background-color: red">
        <v-card class="d-flex pa-2 d-flex align-stretch fill-height" variant="outlined" fill-height rounded="0"
          style="background-color: green">
          <div>flexbox</div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HelloWorld',

  data: () => ({})
}
</script>
