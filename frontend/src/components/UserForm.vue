<template>
    <div class="border border-3 border-dark bg-dark mt-2">
        <form @submit.prevent="createOrUpdateUser">
            <div v-if="incorrectData" class="border my-2">
                <div v-for="field in incorrectFields" :key="field" class="bg-danger d-flex justify-content-center align-items-center">
                    {{ field[0].toUpperCase() }}
                </div>
            </div>
            <div v-if="unmatchedPass" class="border d-flex justify-content-center align-items-center bg-danger">
                <div class="p-4">PASSWORDS DON'T MATCH</div>
            </div>
            <div class="row mt-3">
                <div class="col ms-3">
                    <input v-model="email" class="form-control mb-3" type="email" maxlength="150" placeholder="Email" required>
                </div>
                <div class="col me-3">
                    <input v-model="phone" class="form-control" type="text" maxlength="50" placeholder="+380XXXXXXXXX">
                </div>
            </div>
            <div class="row">
                <div class="col ms-3">
                    <input v-model="firstName" class="form-control mb-3" type="text" maxlength="124" placeholder="First Name" required>
                </div>
                <div class="col me-3">
                    <input v-model="lastName" class="form-control" type="text" maxlength="124" placeholder="Last Name">
                </div>
            </div>
            <div class="row">
                <div class="col ms-3">
                    <input :required="useCase === 'create'"  @input="passwordCheck" v-model="password" class="form-control mb-3" type="password" placeholder="Password">
                </div>
                <div class="col me-3">
                    <input :required="useCase === 'create'" @input="passwordCheck" v-model="password2" class="form-control" type="password" placeholder="Confirm password">
                </div>
            </div>
            <div class="row">
                <div class="col ms-3">
                    <button class="submit-button btn btn-primary mb-3" type="submit">Submit</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import axiosApi from '../axios-api'
export default {
    name: 'user-form',
    props: [
        'idProp', 'emailProp', 'firstNameProp',
        'lastNameProp', 'phoneProp', 'useCase'
    ],
    data() {
        return {
            email: this.emailProp,
            firstName: this.firstNameProp,
            lastName: this.lastNameProp,
            phone: this.phoneProp,
            password: '',
            password2: '',
            unmatchedPass: false,
            incorrectData: false,
            incorrectFields: {}
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
        async createOrUpdateUser(event) {
            if (this.useCase === "create" && !this.unmatchedPass) {
                axiosApi.post("/users/",
                {
                    email: this.email,
                    first_name: this.firstName,
                    last_name: this.lastName || null,
                    phone: this.phone || null,
                    password: this.password
                },
                {
                    headers: {
                        "Authorization": `Bearer ${this.$store.state.userToken}`
                    }
                })
                .then(response => {
                    this.incorrectData = false
                    this.incorrectFields = {}
                    this.$store.dispatch("addUser", response.data)

                    event.target.reset()
                })
                .catch(error => {
                    this.incorrectFields = JSON.parse(error.response.request.responseText);
                    this.incorrectData = true;
                    console.log(error)
                })
            } else if (this.useCase === "update" && !this.unmatchedPass) {
                let properties = {
                    email: this.email,
                    first_name: this.firstName,
                    last_name: this.lastName || null,
                    phone: this.phone || null,
                    password: this.password
                }
                if (!this.password) {
                    delete properties.password
                }
                axiosApi.put(`/users/${this.idProp}/`,
                    properties,
                {
                    headers: {
                        "Authorization": `Bearer ${this.$store.state.userToken}`
                    }
                })
                .then(() => {
                    this.$router.push({ name: "index" })
                })
                .catch(error => {
                    this.incorrectFields = JSON.parse(error.response.request.responseText);
                    this.incorrectData = true;
                    console.log(error)
                })
            }
        }
    }
}
</script>

<style scoped>

</style>
