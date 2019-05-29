import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Top from '@/components/TOP'
import About from '@/components/About'
import HelloWorld from '@/components/TOP'
import Index from '@/pages/Index'
import Index3 from '@/pages/Index3'

import Landing from '@/pages/Landing.vue';
import Login from '@/pages/Login.vue';
import Profile from '@/pages/Profile.vue';
import MainNavbar from '@/layout/MainNavbar.vue';
import MainFooter from '@/layout/MainFooter.vue';


Vue.use(Router)

export default new Router({
  linkExactActiveClass: 'active',
  mode: 'history', //URLにでてくる#をけします。
  routes: [

    {
      path: '/home',
      name: 'Home',
      component: Home
    },

    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    },

    {
      path: '/Top',
      name: 'Top',
      component: Top

    },
    {
      path: '/',
      name: 'index',
      components: { default: Index, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      },
    },
    {
      path: '/login',
      name: 'login',
      components: { default: Login, header: MainNavbar },
      props: {
        header: { colorOnScroll: 400 }
      }
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/index3',
      name: 'index3',
      components: { default: Index3, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      },
    }

  ]
})
