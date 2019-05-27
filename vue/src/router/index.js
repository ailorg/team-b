import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Top from '@/components/TOP'
import Index from '@/pages/Index'
import Landing from '@/pages/Landing.vue';
import Login from '@/pages/Login.vue';
import Profile from '@/pages/Profile.vue';
import MainNavbar from '@/layout/MainNavbar.vue';
import MainFooter from '@/layout/MainFooter.vue';


Vue.use(Router)

export default new Router({
  mode: 'history', //URLにでてくる#をけします。
  routes: [

    {
      path: '/home',
      name: 'Home',
      component: Home
    },

    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },

    {
    path: '/about',
    name: 'About',
    component: About
    },

    {
      path: '/Top',
      name: 'Top',
      component: Top
    },
    {
      path: '/index',
      name: 'index',
      components: { default: Index, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 400 },
        footer: { backgroundColor: 'black' }
      }
    },
  ],
})