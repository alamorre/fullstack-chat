<script setup>
import AuthPage from './pages/AuthPage/index.vue'
import ChatsPage from './pages/ChatsPage/index.vue'
</script>

<template>
  <AuthPage v-if="!user" @onAuth="handleAuth" />
  <ChatsPage v-else v-bind:username="user.username" v-bind:secret="user.secret" />
</template>

<script>
export default {
  data() {
    return {
      user: undefined,
    }
  },
  methods: {
    handleAuth(user) {
      this.user = user;
    },
  },
}
</script>  
