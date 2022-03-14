<template>
  <v-container fluid
    ><v-list>
      <v-list-item v-for="(img, index) in imgUrl" :key="index">
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
            ><v-icon small color="red">mdi-trash-can</v-icon
            ><v-btn @click="testEnvoi">Test envoi</v-btn></v-col
          ></v-row
        >
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
      @change="loadImage"
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
    imgUrl: [],
    imgObj: [],
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
    async testEnvoi() {
      const formData = new FormData()
      console.log(this.imgObj[0].type)
      console.log(typeof this.imgObj[0])
      formData.append('storage', this.imgObj[0], 'Bubobubo_20200611.png')
      formData.append('date', '2022-01-01')
      // const data = { Storage: formData, date: '2022-01-01' }
      await this.$axios.$post('media/', formData, {
        headers: {
          accept: 'application/json',
          'Content-Type': 'multipart/form-data',
        },
      })
      // })
    },
    /**
     * Method to load and display picture before uploading through the API
     *
     * This method is triggered on file selection through v-file-input:
     * - Image url is push to imgUrl array
     * - Image file object is push to imgObj array
     *
     * In case of error, error message display through errorSnackBar component
     */
    loadImage() {
      try {
        if (this.newImg && this.$refs.pictInput.validate()) {
          const reader = new FileReader()
          reader.readAsDataURL(this.newImg)
          reader.addEventListener('load', () => {
            this.imgUrl.push(reader.result)
            this.imgObj.push(this.newImg)
            this.$refs.pictInput.reset()
          })
        }
      } catch (_err) {
        const error = {}
        error.code = errorCodes.imgLoading.code
        error.msg = $nuxt.$t(`error.${errorCodes.imgLoading.msg}`)
        // set error message to errorStore and triggers message displyy through "err" watcher in
        // error-snackbar component
        this.$store.commit('errorStore/setError', error)
      }
    },
  },
}
</script>

<style scoped>
.v-file-input {
  width: 400px;
}
</style>
