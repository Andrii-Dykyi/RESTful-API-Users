import { createRouter, createWebHistory } from 'vue-router'
import Index from '../views/Index.vue'
import Detail from '../views/Detail.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'


const routes = [
  {
    path: '/',
    name: 'index',
    component: Index,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/users/:id/',
    name: 'detail',
    component: Detail,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
