import { createVuetify } from 'vuetify'
import '@mdi/font/css/materialdesignicons.css'
import { VDataTable } from 'vuetify/labs/VDataTable'

export default defineNuxtPlugin((nuxtApp) => {
  const vuetify = createVuetify({
    components: {
      VDataTable
    },
    ssr: true,
    theme: {
      defaultTheme: 'light'
    }
  })
  nuxtApp.vueApp.use(vuetify)
})
