<template>
    <div class="login-wrapper text-center d-flex justify-content-center align-items-center">
        <div class="login-box border border-primary border-3 p-5 bg-dark">
            <form @submit.prevent="registerUser" class="m-5">
                <h1 class="mb-5 text-primary">Register</h1>
                <div v-if="incorrectData" class="border my-2">
                    <div v-for="field in incorrectFields" :key="field" class="bg-danger">
                        {{ field[0].toUpperCase() }}
                    </div>
                </div>
                <div v-if="unmatchedPass" class="border my-2">
                    <div class="p-4 bg-danger">PASSWORDS DON'T MATCH</div>
                </div>
                <input v-model="email" class="form-control mb-2" type="email" maxlength="150" placeholder="Email" required>
                <input v-model="firstName" class="form-control mb-2" type="text" maxlength="124" placeholder="First Name" required>
                <input v-model="lastName" class="form-control mb-2" type="text" maxlength="124" placeholder="Last Name">
                <input v-model="phone" class="form-control mb-2" type="text" maxlength="50" placeholder="+380XXXXXXXXX">
                <input @input="passwordCheck" v-model="password" class="form-control mb-2" type="password" placeholder="Password" required>
                <input @input="passwordCheck" v-model="password2" class="form-control mb-2" type="password" placeholder="Confirm password" required>
                <button class="w-100 btn btn-primary mb-2" type="submit">Submit</button>
                <p class="m-2 text-light">Already have account? Please login!</p>
                <router-link to="login" class="w-100 btn btn-primary" role="button">Login</router-link>
            </form>
        </div>
    </div>
</template>

<script>
import axiosApi from '../axios-api'

export default {
    name: "register",
    data() {
        return {
            email: '',
            firstName: '',
            lastName: '',
            phone: '',
            password: '',
            password2: '',
            incorrectData: false,
            unmatchedPass: false,
            incorrectFields: {},
        }
    },
    methods: {
        passwordCheck() {
            if (this.password != this.password2) {
                this.unmatchedPass = true
            } else {
                this.unmatchedPass = false
            }
        },
        registerUser() {
            if (!this.unmatchedPass) { 
                axiosApi.post("/register/", {
                    email: this.email,
                    first_name: this.firstName,
                    last_name: this.lastName || null,
                    phone: this.phone || null,
                    password: this.password
                })
                .then(() => {
                    this.incorrectData = false
                    this.incorrectFields = {}
                    this.$router.push({ name: "login" })
                })
                .catch(error => {
                    this.incorrectFields = JSON.parse(error.response.request.responseText);
                    this.incorrectData = true;
                })
            } else {
                this.incorrectData = true
            }
        }
    },
}
</script>

<style scoped>
    .login-wrapper {
        height: 100vh;
    }
</style>