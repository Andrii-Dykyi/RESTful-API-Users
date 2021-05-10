<template>
    <div class="container">
        <Navbar />
        <h4 class="text-primary my-3">Update User</h4>
        <UserForm
            v-if="id"
            :idProp="id"
            :emailProp="email"
            :firstNameProp="firstName"
            :lastNameProp="lastName"
            :phoneProp="phone"
            useCase="update"
        />
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import UserForm from "@/components/UserForm.vue"
import axiosApi from '../axios-api'

export default {
    name: "detail",
    components: {
        Navbar,
        UserForm
    },
    data() {
        return {
            id: undefined,
            email: '',
            firstName: '',
            lastName: '',
            phone: '',
        }
    },
    created() {
        this.getUser()
    },
    methods: {
        async getUser() {
            await axiosApi.get(`/users/${this.$route.params.id}/`, {
                headers: {
                    "Authorization": `Bearer ${this.$store.state.userToken}`
                }
            })
            .then(response => {
                this.id = response.data.id
                this.email = response.data.email
                this.firstName = response.data.first_name
                this.lastName = response.data.last_name
                this.phone = response.data.phone
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
