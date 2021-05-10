import { createStore } from 'vuex'
import axiosApi from '../axios-api'


export default createStore({
    state: {
        userToken: localStorage.getItem("accessToken") || null,
        userRefreshToken: localStorage.getItem("refreshToken") || null,
        usersList: []
    },
    getters: {
        loggedIn(state) {
            return state.userToken != null
        },
    },
    mutations: {
        setTokens(state, { access, refresh }) {
            state.userToken = access
            state.userRefreshToken = refresh
            localStorage.setItem("accessToken", access)
            localStorage.setItem("refreshToken", refresh)
        },
        destroyToken(state) {
            state.userToken = null
            state.userRefreshToken = null
            localStorage.removeItem("accessToken")
            localStorage.removeItem("refreshToken")
        },
        setUsers(state, users) {
            state.usersList = users
        },
        addUser(state, user) {
            state.usersList.push(user)
        }
    },
    actions: {
        async userLogin(context, userData) {
            await axiosApi.post("/login/", {
                email: userData.email,
                password: userData.password
            })
            .then(response => {
                context.commit("setTokens", 
                    {
                        access: response.data.access,
                        refresh:  response.data.refresh
                    }
                )
            })
        },
        userLogOut(context) {
            context.commit("destroyToken")
        },
        setUsers(context, users) {
            context.commit("setUsers", users)
        },
        addUser(context, user) {
            context.commit("addUser", user)
        }
    },
    modules: {
    }
})
