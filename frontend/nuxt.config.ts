// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: [
        [
            "@pinia/nuxt",
            {
                autoImports: ["defineStore", "acceptHMRUpdate"],
            },
        ],
        '@invictus.codes/nuxt-vuetify',
        '@nuxtjs/i18n'
    ],
    vuetify: {
        /* vuetify options */
        vuetifyOptions: {
            // @TODO: list all vuetify options
        },
        moduleOptions: {
            /* nuxt-vuetify module options */
            treeshaking: true,
            useIconCDN: true,
            /* vite-plugin-vuetify options */
            styles: true,
            autoImport: true,
        }
    },
    css: [
        "vuetify/lib/styles/main.css",
        "@mdi/font/css/materialdesignicons.min.css",
        "leaflet/dist/leaflet.css",
    ],

    build: {
        transpile: ["vuetify"],
    },
    imports: {
        // Auto-import pinia stores defined in `~/stores`
        dirs: ['stores'],
    },
    i18n: {
        locales: [
            { code: 'en', iso: 'en-US', file: 'en.json' },
            { code: 'fr', iso: 'fr-FR', file: 'fr.json' },
        ],

        defaultLocale: 'fr',
        langDir: 'locales',
    },
    // devtools: {
    //     // Enable devtools (default: true)
    //     enabled: true,
    //     // VS Code Server options
    //     vscode: {},
    //     // ...other options
    // },
    // routeRules: {
    //     '/api/v1/**': { cors: true, headers: { 'access-control-allow-methods': 'GET' }, proxy: 'http://localhost:8000' }
    // },
    runtimeConfig: {
        apiBaseUrl: 'http://localhost:8000',
    },
})
