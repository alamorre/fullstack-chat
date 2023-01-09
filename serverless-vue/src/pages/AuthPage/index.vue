<template>
    <div class="login-page">
        <div class="card" >
            <form @submit.prevent="login">
                <div class="title">Login</div>
                <input placeholder="Username" type="text" v-model="username" />
                <br />
                <input placeholder="Password" type="password" v-model="password" />
                <br />
                <button type="submit">Login</button>
            </form>

            <form @submit.prevent="signup">
                <div class="title">Sign Up</div>
                <input class="input" placeholder="Username" type="text" v-model="username" />
                <br />
                <input placeholder="Password" type="password" v-model="password" />
                <br />
                <input placeholder="Email" type="text" v-model="email" />
                <br />
                <input placeholder="First name" type="text" v-model="first_name" />
                <br />
                <input placeholder="Last name" type="text" v-model="last_name" />
                <br />
                <button type="submit">Sign Up</button>
            </form>
        </div>
    </div>
</template>

<style>
.login-page { width: 100vw; height: 100vh; background: linear-gradient(180deg, rgba(117,84,160,1) 7%, rgba(117,84,160,1) 17%, rgba(106,95,168,1) 29%, rgba(99,103,174,1) 44%, rgba(87,116,184,1) 66%, rgba(70,135,198,1) 83%, rgba(44,163,219,1) 96%, rgba(22,188,237,1) 100%, rgba(0,212,255,1) 100%); }
.card { width: 200px; position: relative; left: calc(50vw - 100px); text-align: center; padding-top: 6vw;  }
.title { padding-top: 32px; font-size: 22px; color: white; font-weight: 700; }
input { width: calc(100% - 16px); margin-top: 12px; padding: 8px; background-color: #e6f7ff; outline: none; border: 1px solid #e6f7ff; }
button { margin-top: 12px; width: 100%; padding: 8px; }
</style>
  
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