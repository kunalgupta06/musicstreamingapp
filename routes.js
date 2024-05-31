import LandingPage from './components/LandingPage.vue'
import SignUp from './components/SignUp.vue'
import loginPage from './components/login.vue'

import { createRouter, createWebHistory} from 'vue-router'

const routes=[
    {
        name:'LandingPage',
        component:LandingPage,
        path:'/',

    },
    {
        name:'SignUp',
        component:SignUp,
        path:'/signup',

    },
    {
        name:'login',
        component:loginPage,
        path:'/login',

    },

]
const router=createRouter({
    history:createWebHistory(),
    routes
})
export default router