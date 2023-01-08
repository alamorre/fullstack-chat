<script setup>
import AuthPage from './pages/AuthPage/index.vue'
</script>

<template>
  <AuthPage @onAuth="handleAuth" />
</template>

<script>
export default {
  methods: {
    handleAuth(user) {
      console.log(`User: ${user}`)
    },
  },
}
</script>  
