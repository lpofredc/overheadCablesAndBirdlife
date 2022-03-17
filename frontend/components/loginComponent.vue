<template>
  <v-row justify="center" class="mt-16">
    <v-form ref="form" v-model="valid" class="mt-5 ml-4">
      <v-card min-width="400" class="pa-5 pb-10">
        <v-row justify="center" class="my-5"
          ><div>{{ $t('login.sign-in') }}</div></v-row
        >
        <v-row justify="start">
          <v-icon large class="mx-3">mdi-account-circle</v-icon>
          <v-text-field
            v-model="login.username"
            :rules="nameRules"
            type="text"
            class="pl-3 pr-5"
            filled
            required
            @keyup.enter="userLogin"
          ></v-text-field>
        </v-row>

        <v-row justify="start" class="mb-3">
          <v-icon large class="mx-3">mdi-lock</v-icon>
          <v-text-field
            v-model="login.password"
            :rules="pwdRules"
            type="password"
            filled
            class="pl-3 pr-5"
            required
            @keyup.enter="userLogin"
          ></v-text-field>
        </v-row>
        <v-row justify="space-around" class="mt-10">
          <v-btn width="150" color="info" @click="reset">
            {{ $t('app.cancel') }}
          </v-btn>
          <v-btn width="150" color="primary" @click="userLogin">
            {{ $t('login.sign-in') }}
          </v-btn>
        </v-row>
      </v-card>
    </v-form>
  </v-row>
</template>

<script>
export default {
  name: 'LoginComponent',
  auth: false,
  data() {
    return {
      valid: true,
      login: {
        username: '',
        password: '',
      },
      nameRules: [(v) => !!v || this.$t('login.required_username_msg')],
      pwdRules: [(v) => !!v || this.$t('login.required_pwd_msg')],
    }
  },
  methods: {
    reset() {
      this.$refs.form.reset()
    },
    /**
     * Login method based on form data.
     * Managed by auth module that requests login to the backend API.
     */
    async userLogin() {
      try {
        // check theform is validated
        if (this.$refs.form.validate()) {
          await this.$auth.loginWith('local', {
            data: this.login,
          })
          this.$router.push('/view') // if OK, redirect to "/view"
        }
      } catch (err) {
        const error = {}
        // if nuxt error message contains substring '401'
        if (err.toString().includes('401')) {
          error.code = errorCodes.authentication.code
          error.msg = $nuxt.$t(`error.${errorCodes.authentication.msg}`)
        } else {
          // for other login errors
          error.code = errorCodes.login.code
          error.msg = $nuxt.$t(`error.${errorCodes.login.msg}`)
        }
        // set error message to errorStore and triggers message displyy through "err" watcher in
        // error-snackbar component
        this.$store.commit('errorStore/setError', error)
      }
    },
  },
}
</script>
