import axios from 'axios'
import router from '../src/router/index'


const axiosApi = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1",
    headers: {
        "Content-Type": "application/json"
    }
})

axiosApi.interceptors.response.use(response => {
    // If unauthorized request or token expires link to login
    // Token refresh isn't realized in this version
    if (response.status === 401) {
        router.push({ name: "login" })
    }
    return response
})


export default axiosApi