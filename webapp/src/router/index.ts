import { createRouter, createWebHistory } from 'vue-router'
import apiService from '@/services/Apiservices'
import { useAppStore } from '@/stores/app'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/home',
      name: 'home',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/HomeView.vue')
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  const appStore = useAppStore()
  if (to.name === 'login') {
    if (localStorage.getItem('system_tcc') == null) {
      next()
    } else {
      try {
        const user = await apiService.getUser()
        appStore.setUser(user)
        appStore.setAuthenticated(true)
        next({ name: 'home' })
      } catch (error) {
        localStorage.removeItem('system_tcc')
        appStore.setUser(null)
        appStore.setAuthenticated(false)
        next()
      }
    }
  } else if (appStore.authenticated === false) {
    if (localStorage.getItem('system_tcc') == null) {
      next({ name: 'login' })
    } else {
      try {
        const user = await apiService.getUser()
        appStore.setUser(user)
        appStore.setAuthenticated(true)
        next();
      } catch (error) {
        localStorage.removeItem('system_tcc')
        appStore.setAuthenticated(false)
        appStore.setUser(null)
        next({ name: 'login' })
      }
    }
  } else if (appStore.authenticated && to.name !== 'login') {
    next()
  } else {
    next({ name: 'home' })
  }
})

export default router
