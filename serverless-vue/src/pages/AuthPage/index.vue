<template>
    <div>
        <form @submit.prevent="login">
            <label>Username: </label>
            <input type="text" v-model="username" />
            <br />
            <label>Password: </label>
            <input type="password" v-model="password" />
            <br />
            <button type="submit">Login</button>
        </form>
    </div>
</template>
  
<script>
import { signup } from './api'

export default {
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        login() {
            signup(this.username, this.password);
            this.$emit('onAuth', `${this.username} + ${this.password}`, );
        },
    },
}
</script>  