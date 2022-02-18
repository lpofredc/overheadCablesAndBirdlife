<template>
  <v-row justify="center" class="mt-16">
    <v-form ref="form" v-model="valid" class="mt-16 ml-10">
      <v-card width="400" class="pa-5 pb-10">
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
            required
          ></v-text-field>
        </v-row>

        <v-row justify="start" class="mb-3">
          <v-icon large class="mx-3">mdi-lock</v-icon>
          <v-text-field
            v-model="login.password"
            :rules="pwdRules"
            type="password"
            class="pl-3 pr-5"
            required
          ></v-text-field>
        </v-row>
        <v-row justify="space-around" class="mt-10">
          <v-btn width="150" color="info" @click="reset">
            {{ $t('login.cancel') }}
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
  name: 'LoginPage',
  auth: false,
  data() {
    return {
      valid: true,
      login: {
        username: '',
        password: '',
        // username: 'sylvain',
        // password: 'sylvain',
      },
      nameRules: [(v) => !!v || this.$t('login.required_username_msg')],
      pwdRules: [(v) => !!v || this.$t('login.required_pwd_msg')],
    }
  },
  methods: {
    reset() {
      this.$refs.form.reset()
    },

    async userLogin() {
      try {
        this.$refs.form.validate()
        await this.$auth.loginWith('local', {
          data: this.login,
        })
        // this.$store.commit('setConnectedStatus', true)
        this.$router.push('/main')
      } catch (err) {
        console.log(err)
      }
    },
  },
}
</script>
