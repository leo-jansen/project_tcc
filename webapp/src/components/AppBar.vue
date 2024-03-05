<template>
  <v-app-bar flat color="#074293" :elevation="0">
    <template v-slot:prepend>
      <v-img :src="logo" :width="100" style="cursor: pointer" />
    </template>

    <v-toolbar-title>
      <div v-if="showMenu">
        <DxMenu
          :data-source="menu"
          :show-first-submenu-mode="showSubmenuModes.name"
          orientation="horizontal"
          :hide-submenu-on-mouse-leave="false"
          display-expr="name"
          @item-click="itemClick"
        />
      </div>
    </v-toolbar-title>

    <template v-slot:append>
      <div v-if="showMenu">
        <span class="fa fa-sign-out-alt" :onclick="logout">
          <v-img :src="logoutIco" :width="20" style="cursor: pointer" />
        </span>
      </div>
    </template>
  </v-app-bar>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'
import DxMenu from 'devextreme-vue/menu'
import logo from '@/assets/logo.svg'
import logoutIco from '@/assets/logout.svg'

export default defineComponent({
  name: 'app-bar',
  components: { DxMenu },
  setup() {
    const appStore = useAppStore()
    const router = useRouter()

    const showMenu = computed(() => appStore.authenticated)

    const menu = [
      {
        id: 1,
        name: 'Administrador',
        items: [
          {
            id: '1_1',
            name: 'Gerenciar Usuarios'
          }
        ]
      }
    ]

    const showSubmenuModes = {
      name: 'onHover',
      delay: { show: 0, hide: 500 }
    }

    function itemClick(e: any) {
      if (e.itemData.name == 'Gerenciar Usuarios') {
        router.push('/administrador')
      }
    }

    function logout() {
      localStorage.removeItem('system_tcc')
      appStore.setUser(null)
      appStore.setAuthenticated(false)
      router.push('/')
    }

    return {
      menu,
      showSubmenuModes,
      logo,
      logout,
      logoutIco,
      showMenu,
      itemClick
    }
  }
})
</script>
<style>
.fa {
  height: 64px;
}
</style>
