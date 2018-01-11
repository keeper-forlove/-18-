import Vue from 'vue'
import Router from 'vue-router'
import AppMain from '@/components/AppMain'
import AppMine  from "@/components/mine/AppMine"
import AppSet  from "@/components/mine/AppSet"
import AppMessage from "@/components/mine/AppMessage"
import AppLogin from "@/components/login/AppLogin"
import AppRegister from "@/components/register/AppRegister"
import AppReset from "@/components/resetpassward/AppReset"
Vue.use(Router)

export default new Router({
  routes: [
    {path: '/main',name: 'main',component: AppMain},
    {path: '/mine',name: 'mine',component: AppMine},
    {path: '/app-set',name: 'set',component: AppSet},
    {path: '/app-message',name: 'message',component: AppMessage},
    {path: '/login',name: 'login',component: AppLogin},
    {path: '/register',name: 'register',component: AppRegister},
    {path: '/reset',name: 'reset',component: AppReset}           
  ]
})
