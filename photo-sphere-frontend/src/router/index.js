import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import UserProfile from '@/views/UserProfile.vue'
import Organization from '@/views/Organization.vue'
import PhotoDetails from '@/views/PhotoDetails.vue'
import AlbumDetails from '@/views/AlbumDetails.vue'
import MarketPlace from '@/views/MarketPlace.vue'

const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/user-profile/:id',
        name: 'User-Profile',
        component: UserProfile
    },
    {
        path: '/organization/:id',
        name: 'Organization',
        component: Organization
    },
    {
        path: '/photo/:id',
        name: 'Photo-Details',
        component: PhotoDetails
    },
    {
        path: '/album/:id',
        name: 'Album-Details',
        component: AlbumDetails
    },
    {
        path: '/exhibitions',
        name: 'Exhibitions',
        component: Home
    },
    {
        path: '/marketplace',
        name: 'Marketplace',
        component: MarketPlace
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router