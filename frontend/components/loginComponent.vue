<template>
  <v-card flex>
    <v-form ref="form" v-model="valid">
      <v-toolbar dark color="light-blue darken-4">
        <v-btn icon dark @click="closeDialog">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-toolbar-title>{{ $t('login.sign-in') }}</v-toolbar-title>
      </v-toolbar>
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
            <v-col cols="12" class="justify-center">
              Mot de passe oublié?</v-col
            >
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-btn color="success" block @click="userLogin" large>
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
  props: {
    dialog: { type: Boolean },
  },
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
    closeDialog() {
      this.$emit('close-dialog')
    },
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
