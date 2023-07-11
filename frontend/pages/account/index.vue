<script setup lang="ts">
definePageMeta({ middleware: 'auth' })
const reveal = ref(false)
const { user, loggedIn } = useAuth()
</script>

<template>
  <v-card class="mx-auto" width="90%">
    <v-card-text v-if="loggedIn && user">
      <div>{{ user.email }}</div>
      <p class="text-h4 text--primary">
        {{ user.username }}
      </p>
      <p>{{ user.first_name }} {{ user.last_name }}</p>
    </v-card-text>
    <v-card-text v-else>
      Not connected
    </v-card-text>
    <v-card-actions v-if="!reveal">
      <v-btn variant="text" color="teal-accent-4" @click="reveal = true">
        Learn More
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <v-card v-if="reveal" class="v-card--reveal" style="height: 100%">
        <v-card-text class="pb-0">
          <p>
          <pre><code>{{ user }}</code></pre>
          </p>
        </v-card-text>
        <v-card-actions class="pt-0">
          <v-btn variant="text" color="teal-accent-4" @click="reveal = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-expand-transition>
  </v-card>
</template>
