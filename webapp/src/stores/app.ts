import type { UserIn } from '@/types/Administracao';
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    user: {} as UserIn | null,
    authenticated: false,
  }),
  actions: {
    setAuthenticated(state: boolean) {
      this.authenticated = state;
    },
    setUser(state: UserIn | null) {
      this.user = state;
      this.authenticated = true;
    }
  }
})