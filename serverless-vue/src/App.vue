<script setup>
import AuthPage from './pages/AuthPage/index.vue'
</script>

<template>
  <div v-if="user">chats...</div>
  <div v-else><AuthPage @onAuth="handleAuth" /></div>
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
