import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import Top from '@/components/TOP'
import Index from '@/pages/Index'

Vue.use(Router)

export default new Router({
  mode: 'history', //URLにでてくる#をけします。
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/home',
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
      name: 'Index',
      component: Index
    },
  ],
})