<template>
  <v-container fluid
    ><v-list>
      <v-list-item v-for="(img, index) in images" :key="index">
        <v-row
          ><v-col
            ><v-img
              :src="img"
              max-height="100"
              max-width="166"
              class="ma-2" /></v-col
          ><v-col>date: {{ pictDate }}</v-col
          ><v-col></v-col
          ><v-col cols="1"
            ><v-icon small color="red">mdi-trash-can</v-icon></v-col
          ></v-row
        >
      </v-list-item>
    </v-list>
    <!-- <v-container class="d-flex space-around flex-wrap mx-2">
      <v-card
        v-for="(img, index) in images"
        :key="index"
        width="350px"
        heigth="200px"
        class="strech ma-2"
      >
        <v-row
          ><v-col
            ><v-img
              :src="img"
              max-height="75"
              max-width="125"
              class="ma-2" /></v-col
          ><v-col
            ><v-icon small color="red">mdi-trash-can</v-icon> -->
    <!-- <v-menu
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              ><template #activator="{ on, attrs }">
                <v-text-field
                  v-model="pictDate"
                  :label="$t('point.datecreate')"
                  persistent-hint
                  prepend-icon="mdi-calendar"
                  readonly
                  dense
                  class="pa-2"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="pictDate"
                no-title
              ></v-date-picker> </v-menu
            > -->
    <!-- <v-text-field
              ref="lat"
              v-model="lat"
              :label="$t('point.latitude')"
              :disabled="!manualChange"
              type="number"
              :rules="[rules.requiredOrNotValid, rules.latRange]"
              required
              hide-spin-buttons
              class="shrink mx-5" /></v-col
        ></v-row>
        <v-row>
          <v-textarea
            v-model="remark"
            clearable
            clear-icon="mdi-close-circle"
            :label="$t('point.remark')"
            class="mx-5"
          ></v-textarea
        ></v-row> </v-card
    ></v-container> -->
    <!-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-->
    <!-- <v-container class="d-flex space-around flex-wrap mx-2">
      <v-card
        v-for="(img, index) in images"
        :key="index"
        width="350px"
        heigth="200px"
        class="strech ma-2"
      >
        <v-row
          ><v-col
            ><v-img
              :src="img"
              max-height="75"
              max-width="125"
              class="ma-2" /></v-col
          ><v-col
            ><v-icon small color="red">mdi-trash-can</v-icon> <v-text-field
              ref="lat"
              v-model="lat"
              :label="$t('point.latitude')"
              :disabled="!manualChange"
              type="number"
              :rules="[rules.requiredOrNotValid, rules.latRange]"
              required
              hide-spin-buttons
              class="shrink mx-5" /></v-col
        ></v-row>
        <v-row>
          <v-textarea
            v-model="remark"
            clearable
            clear-icon="mdi-close-circle"
            :label="$t('point.remark')"
            class="mx-5"
          ></v-textarea
        ></v-row> </v-card
    ></v-container> -->
    <v-file-input
      ref="pictInput"
      v-model="newImg"
      :rules="rules"
      :clearable="true"
      accept="image/png, image/jpeg, image/bmp"
      prepend-icon="mdi-camera"
      :label="$t('picture.add_file')"
      hide-input
      @change="uploadImage"
    ></v-file-input>
  </v-container>
</template>

<script>
export default {
  name: 'PictureComponent',
  data: () => ({
    newImg: null,
    pictDate: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      .toISOString()
      .substr(0, 10),
    images: [],
    rules: [
      (value) =>
        !value || value.size < 200000000 || $nuxt.$t('picture.add_file'),
    ],
  }),
  methods: {
    uploadImage() {
      if (this.newImg && this.$refs.pictInput.validate()) {
        const reader = new FileReader()
        reader.readAsDataURL(this.newImg)
        reader.addEventListener('load', () => {
          this.images.push(reader.result)
        })
        this.$refs.pictInput.reset()
      }
    },
  },
}
</script>
