<template>
  <v-card>
    <v-form ref="form" v-model="valid">
      <v-card-title class="text-h5 light-blue">
        <v-icon>mdi-account-circle</v-icon>{{ $t('login.sign-in') }}
      </v-card-title>
      <v-card-text>
        <v-container id="input-usage" fluid>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="login.username"
                :rules="nameRules"
                prepend-icon="mdi-account-circle"
                type="text"
                outlined
                fluid
                required
                @keyup.enter="userLogin"
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="login.password"
                :rules="pwdRules"
                prepend-icon="mdi-lock"
                type="password"
                outlined
                required
                @keyup.enter="userLogin"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions class="grey lighten-2">
        <v-btn color="error" @click="reset">
          {{ $t('app.cancel') }}
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn color="success" @click="userLogin">
          {{ $t('login.sign-in') }}
        </v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import * as errorCodes from '~/static/errorConfig.json'

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
