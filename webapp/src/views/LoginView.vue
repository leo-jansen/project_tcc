<template>
  <div class="home">
    <FormLogin/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import FormLogin from "@/components/FormLogin.vue";

export default defineComponent({
  name: "LoginView",
  components: {
    FormLogin
  },
});
</script>

<style scoped>
/* Estilos específicos para este componente */
</style>