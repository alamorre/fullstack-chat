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

        <form @submit.prevent="signup">
            <label>Username: </label>
            <input type="text" v-model="username" />
            <br />
            <label>Password: </label>
            <input type="password" v-model="password" />
            <br />
            <label>Email: </label>
            <input type="text" v-model="email" />
            <br />
            <label>First name: </label>
            <input type="text" v-model="first_name" />
            <br />
            <label>Last name: </label>
            <input type="text" v-model="last_name" />
            <br />
            <button type="submit">Sign Up</button>
        </form>
    </div>
</template>
  
<script>
import { loginRest, signupRest } from './api'

export default {
    data() {
        return {
            username: '',
            password: '',
            email: '',
            first_name: '',
            last_name: '',
        }
    },
    methods: {
        login() {
            loginRest(this.username, this.password)
            .then(response => this.$emit('onAuth', { ...response.data, secret: this.password } ))
            .catch(error => console.log('Login error', error));
        },
        signup() {
            signupRest(this.username, this.password, this.email, this.first_name, this.last_name)
            .then(response => this.$emit('onAuth', { ...response.data, secret: this.password } ))
            .catch(error => console.log('Sign up error', error));
        },
    },
}
</script>  