<template>
  <div class="mx-5">
    <v-card class="elevation-1 mx-auto mt-10" max-width="600">
      <v-alert color="red" dismissible prominent type="error" v-if="visivel"
        >Usuario ou senha invalidos</v-alert
      >
      <v-toolbar dark color="primary">
        <v-toolbar-title>Faça Seu Login</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="login"
            prepend-icon="mdi-account"
            name="login"
            label="Insira Seu Usuario"
            type="text"
          />
          <v-text-field
            v-model="password"
            id="password"
            prepend-icon="mdi-lock"
            name="password"
            label="Digite Sua Senha"
            type="password"
          />
        </v-form>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn color="grey" outlined>Cancelar</v-btn>
        <v-btn color="primary" @click="handleLogin">CONFIRMAR</v-btn>
      </v-card-actions>
    </v-card>
    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAppStore } from '@/stores/app'
import apiService from '@/services/Apiservices'

export default defineComponent({
  name: 'form-login',
  components: {},
  setup() {
    const appStore = useAppStore()
    const router = useRouter()

    const dialog = ref(true)
    const overlay = ref(false)
    const login = ref('')
    const password = ref('')
    const visivel = ref(false)

    function handleLogin() {
      overlay.value = true
      apiService
        .login(login.value, password.value)
        .then((resp) => {
          localStorage.setItem('system_tcc', resp.access_token)
          appStore.setUser(resp.user)
          overlay.value = false
          router.push('/home')
        })
        .catch(() => {
          overlay.value = false
          visivel.value = true
          setTimeout(() => {
            visivel.value = false
          }, 3000)
        })
    }

    return {
      dialog,
      overlay,
      login,
      password,
      visivel,
      handleLogin
    }
  }
})
</script>
