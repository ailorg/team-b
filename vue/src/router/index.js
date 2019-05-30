import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Top from '@/components/TOP'
import About from '@/components/About'
import HelloWorld from '@/components/TOP'
import Index from '@/pages/Index'


import MainNavbar from '@/layout/MainNavbar.vue';
import MainFooter from '@/layout/MainFooter.vue';


Vue.use(Router)

export default new Router({
  mode: 'history', //URLにでてくる#をけします。
  routes: [

    {
      path: '/',
      name: 'Home',
      component: Home
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
      },
    },
    
    {
      path: '/about',
      name: 'About',
      component: About
    }

  ]
})