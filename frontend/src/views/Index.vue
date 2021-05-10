<template>
    <div class="index">
        <div class="container">
            <Navbar />
            <h4 class="text-primary my-3">Create New User</h4>
            <UserForm
                emailProp=""
                firstNameProp=""
                lastNameProp=""
                phoneProp=""
                useCase="create"
            />
            <table class="table table-dark table-hover caption-top text-center mt-2">
                <caption>
                    <h4 class="text-primary">List of users</h4>
                </caption>
                <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">First</th>
                        <th scope="col">Email</th>
                        <th scope="col">Detail</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in usersList" :key="user.id">
                        <th scope="row">{{ user.id }}</th>
                        <td>{{ user.first_name }}</td>
                        <td>{{ user.email }}</td>
                        <td>
                            <router-link :to="{name: 'detail', params: {id: user.id}}">Link</router-link>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import Navbar from "@/components/Navbar.vue"
import UserForm from "@/components/UserForm.vue"
import axiosApi from '../axios-api'


export default {
    name: "Index",
    components: {
        Navbar,
        UserForm
    },
    computed: mapState(["usersList"]),
    created() {
        this.getUsers()
    },
    methods: {
        async getUsers() {
            await axiosApi.get("/users/", {
                headers: {
                    "Authorization": `Bearer ${this.$store.state.userToken}`
                }
            })
            .then(response => {
                this.$store.dispatch("setUsers", response.data)
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
    .submit-button {
        width: 150px;
    }
</style>