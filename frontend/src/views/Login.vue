<template>
    <div class="login-wrapper text-center d-flex justify-content-center align-items-center">
        <div class="login-box border border-primary border-3 p-5 bg-dark">
            <form @submit.prevent="login" class="m-5">
                <h1 class="mb-5 text-primary">Login</h1>
                <div v-if="incorrectAuth" class="border my-2">
                    <div class="p-4 bg-danger">Please enter correct credentials</div>
                </div>
                <input v-model="email" class="form-control mb-2" type="email" maxlength="150" placeholder="Email" required>
                <input v-model="password" class="form-control mb-2" type="password" required autocomplete="on" placeholder="Password">
                <button class="w-100 btn btn-primary mb-2" type="submit">Submit</button>
                <p class="m-2 text-light">Don't have account? Please register!</p>
                <router-link to="register" class="w-100 btn btn-primary" role="button">Register</router-link>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: "login",
    data() {
        return {
            email: '',
            password: '',
            incorrectAuth: false
        }
    },
    methods: {
        async login(event) {
            this.$store.dispatch('userLogin', {
                email: this.email,
                password: this.password
            })
            .then(() => {
                this.$router.push({ name: "index" })
            })
            .catch(() => {
                event.target.reset()
                this.incorrectAuth = true
            })
        }
    }  
}
</script>

<style scoped>
    .login-wrapper {
        height: 100vh;
    }
</style>