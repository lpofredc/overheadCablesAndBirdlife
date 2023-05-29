<template>
  <v-sheet width="600" class="mx-auto">
    <v-form ref="loginForm" v-model="valid">
      <v-text-field v-model="login.username" :rules="nameRules" prepend-icon="mdi-account-circle" type="text" outlined
        fluid required @keyup.enter="userLogin" />

      <v-text-field v-model="login.password" :rules="pwdRules" prepend-icon="mdi-lock" type="password" outlined required
        @keyup.enter="userLogin"></v-text-field>

      <v-btn :disabled="!valid" color="success" class="mt-4" block @click="userLogin()" size="large">{{
        $t('login.sign-in')
      }}</v-btn>
    </v-form>
  </v-sheet>
</template>

<script setup type="ts">
import * as errorCodes from '~/static/errorConfig.json'
import { useErrorsStore } from '~/store/errorStore'

const { t } = useI18n()
const router = useRoute()


const errorStore = useErrorsStore()
const auth = useAuth()
// interface Login {
//   username: string,
//   password: string,
// }
const loginForm = ref(null)
const valid = ref(false)
const login = reactive({
  username: '',
  password: ''
})
const nameRules = reactive([v => !!v || t('login.required_username_msg')])
const pwdRules = reactive([v => !!v || t('login.required_pwd_msg')])


const userLogin = async () => {
  try {
    // check theform is validated
    if (valid) {
      console.log('Try Auth', login)
      await auth.loginWith('local', {
        body: login
      })
      router.push('/view') // if OK, redirect to "/view"
    }
  } catch (err) {
    const error = {}
    // if nuxt error message contains substring '401'
    if (err.toString().includes('401')) {
      error.code = errorCodes.authentication.code
      error.msg = t(`error.${errorCodes.authentication.msg}`)
    } else {
      // for other login errors
      error.code = errorCodes.login.code
      error.msg = t(`error.${errorCodes.login.msg}`)
    }
    // set error message to errorStore and triggers message displyy through "err" watcher in
    // error-snackbar component
    errorStore.setError(error)
  }
}
</script>
