<template>
    <nav class="navbar-expand-lg navbar navbar-dark bg-dark">
        <div class="container">
            <router-link to="/" class="navbar-brand text-primary">User RESTful API</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0"></ul>
                <a @click="logOutUser" class="nav-link" href="#">Logout</a>
            </div>
        </div>
    </nav>
</template>

<script>
import { io } from "socket.io-client"

export default {
    name: 'navbar',
    data() {
        return {
            socket: undefined
        }
    },
    created() {
        this.socket = io('ws://127.0.0.1:8000/')

        this.socket.on("message", (data) => {
            this.$toast.show(`User ${data.user} been updated!!!`, {
                position: "top"
            })
        })
    },
    unmounted() {
        this.socket.disconnect()
    },
    methods: {
        logOutUser() {
            this.$store.dispatch("userLogOut")
            .then(() => {
                this.$router.push({ name: "login" })
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
    .nav-link {
        color: red;
    }
</style>