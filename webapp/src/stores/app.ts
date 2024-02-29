import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    user: null as any,
    authenticated: false,
  }),
  actions: {
    setAuthenticated(state: boolean) {
      this.authenticated = state;
    },
    setUser(state: any) {
      this.user = state;
    }
  }
})