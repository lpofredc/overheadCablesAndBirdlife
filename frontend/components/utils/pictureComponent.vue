<template>
  <v-container fluid>
    <v-list>
      <v-list-item v-for="(img, index) in imgFileContent" :key="index">
        <v-row>
          <v-col>
            <v-img :src="img" max-height="100" max-width="166" class="ma-2" />
          </v-col>
          <v-col>date: {{ pictDate }}</v-col>
          <v-col></v-col>
          <v-col cols="1">
            <v-icon small color="red">mdi-trash-can</v-icon>
          </v-col>
        </v-row>
      </v-list-item>
    </v-list>
    <v-file-input
      ref="pictInput"
      v-model="newImg"
      :rules="rules"
      :clearable="true"
      accept="image/png, image/jpeg, image/bmp"
      prepend-icon="mdi-camera"
      :label="$t('picture.add_file')"
      @change="displayImage"
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
    imgFileContent: [],
    imgFileObject: [],
    showError: false,
    rules: [
      (value) =>
        !value ||
        value.size < 200000 ||
        `${$nuxt.$t('forms.too_big_file')} 200 Ko`,
      (value) =>
        !value ||
        value.type.startsWith('image/') ||
        $nuxt.$t('picture.add_file'),
    ],
  }),
  methods: {
    /**
     * displayImage(): Method to load and display picture before uploading through the API
     *
     * This method is triggered on file selection through v-file-input:
     * - Image file content is push to imgFileContent array
     * - Image file object is push to imgFileObject array
     *
     * In case of error, error message display through errorSnackBar component
     */
    displayImage() {
      try {
        if (this.newImg && this.$refs.pictInput.validate()) {
          const reader = new FileReader()
          reader.readAsDataURL(this.newImg)
          // event listener on successful loading,
          reader.addEventListener('load', () => {
            this.imgFileContent.push(reader.result) // file content push to array
            this.imgFileObject.push(this.newImg) // File object push to array
            this.$refs.pictInput.reset() // reset v-file-input
          })
        }
      } catch (_err) {
        const error = {}
        error.code = errorCodes.img_loading.code
        error.msg = $nuxt.$t(`error.${errorCodes.img_loading.msg}`)
        // set error message to errorStore and triggers message display through "err" watcher in
        // error-snackbar component
        this.$store.commit('errorStore/setError', error)
      }
    },
  },
}
</script>

