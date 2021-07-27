import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import UserProfile from '@/views/UserProfile.vue'
import Organizations from '@/views/Organizations.vue'
import OrganizationDetails from '@/views/OrganizationDetails.vue'
import Exhibitions from '@/views/Exhibitions.vue'
import ExhibitionDetails from '@/views/ExhibitionDetails.vue'
import PhotoDetails from '@/views/PhotoDetails.vue'
import AlbumDetails from '@/views/AlbumDetails.vue'
import MarketPlace from '@/views/MarketPlace.vue'
import Success from '@/components/payment/Success.vue'
import Failure from '@/components/payment/Failure.vue'
import Cancel from '@/components/payment/Cancel.vue'


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
        path: '/organizations',
        name: 'Organizations',
        component: Organizations
    },
    {
        path: '/organization/:id',
        name: 'Organization-Details',
        component: OrganizationDetails
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
        component: Exhibitions
    },
    {
        path: '/exhibition/:id',
        name: 'Exhibition-Details',
        component: ExhibitionDetails
    },
    {
        path: '/marketplace',
        name: 'Marketplace',
        component: MarketPlace
    },
    {
        path: '/payment/success/:id',
        name: 'Order-Success',
        component: Success
    },
    {
        path: '/payment/failed/:id',
        name: 'Order-Failure',
        component: Failure
    },
    {
        path: '/payment/canceled/:id',
        name: 'Order-Cancel',
        component: Cancel
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