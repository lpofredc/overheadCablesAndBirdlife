<template >
    <v-layout full-height>
        <v-app-bar density="compact" color="blue-grey-lighten-5">
            <v-app-bar-title>
                {{ $t('line.line') }}
                <strong>{{ data.properties.owner.label }}</strong>
            </v-app-bar-title>

            <v-app-bar-nav-icon>
                <v-btn density="compact" icon="mdi-close" @click="$router.back()" />
            </v-app-bar-nav-icon>
        </v-app-bar>
        <v-main scrollable>
            <v-container>
            </v-container>
        </v-main>
    </v-layout>
</template>

<script setup lang="ts">
const {data}=defineProps(['data'])
</script>
