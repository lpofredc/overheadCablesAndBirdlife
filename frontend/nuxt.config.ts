// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: [
        '@nuxt-alt/auth',
        '@pinia/nuxt',
        [
            '@pinia/nuxt',
            {
                autoImports: ['defineStore', 'acceptHMRUpdate']
            }
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
            autoImport: true
        }
    },
    css: [
        'vuetify/lib/styles/main.css',
        '@mdi/font/css/materialdesignicons.min.css',
        'leaflet/dist/leaflet.css'
    ],

    build: {
        transpile: ['vuetify']
    },
    imports: {
        // Auto-import pinia stores defined in `~/stores`
        dirs: ['stores']
    },
    i18n: {
        locales: [
            { code: 'en', iso: 'en-US', file: 'en.json' },
            { code: 'fr', iso: 'fr-FR', file: 'fr.json' }
        ],

        defaultLocale: 'fr',
        langDir: 'locales'
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
        public: {
            apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000'
        }
    },
    auth: {
        // cookie: false,
        // redirect: {
        //     login: '/',
        //     logout: '/',
        //     home: '/'
        // },
        globalMiddleware: true,
        strategies: {
            local: {
                scheme: 'refresh',
                token: {
                    property: 'access', // property name of access token get from Back-end
                    global: true,
                    required: true,
                    type: 'JWT'
                },
                user: {
                    property: false,
                    autoFetch: true
                },
                refreshToken: {
                    // it sends request automatically when the access token expires, and its expire time has set on the Back-end
                    property: 'refresh', // property name of refresh token get from Back-end
                    data: 'refresh' // data can be used to set the name of the property you want to send in the request.
                },
                endpoints: {
                    login: {
                        url: '/api/v1/auth/jwt/create/',
                        method: 'post'
                    },
                    refresh: { url: '/api/v1/auth/jwt/refresh', method: 'post' },
                    logout: false, //  there is no endpoint for logout in API. Just remove the token from localstorage
                    user: {
                        url: '/api/v1/auth/users/me/',
                        method: 'get',
                        property: true
                    }
                }
            }
        }
    }
})
