<template>
  <v-sheet class="fill-height" dark align-self="start">

    <v-list class="pa-0 bg-surface-variant overflow-y-auto fill-height" v-if="posts && posts.length > 0" lines="three">
      <v-list-item v-for="post in posts" :key="post.id" :to="`/posts/${post.id}`"
        prepend-avatar="https://cdn.vuetifyjs.com/images/arthur.png">
        <v-list-item-title>
          {{ post.title }}
        </v-list-item-title>
        <v-list-item-subtitle>
          <i>{{new Date(post.timestamp_create).toISOString().substr(0,10)}}</i> - {{ post.intro }}
        </v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-sheet>
</template>

<script setup>
const { data: posts } = await useHttp('/api/v1/custom-content/news/')
console.log('POSTS', posts.value[0])
</script>
