<template>
  <v-card class="mx-auto">
    <v-card-title>News</v-card-title>
    <v-list v-if="posts.length > 0">
      <v-list-item-group>
        <v-list-item
          v-for="post in posts"
          :key="post.id"
          :to="`/posts/${post.id}`"
        >
          <v-list-item-content>
            <v-list-item-title>
              {{ post.title }}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ post.intro }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: 'PostsList',
  auth: false,
  data: () => ({
    posts: [
      {
        icon: 'mdi-wifi',
        text: 'Wifi',
      },
      {
        icon: 'mdi-bluetooth',
        text: 'Bluetooth',
      },
      {
        icon: 'mdi-chart-donut',
        text: 'Data Usage',
      },
    ],
    model: 1,
  }),
  mounted() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      this.posts = await this.$axios.$get('/custom-content/news/')
    },
  },
}
</script>
