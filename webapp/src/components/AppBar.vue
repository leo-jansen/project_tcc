<template>
  <v-app-bar flat color="#074293">
    <v-toolbar-title>
      <v-img :src="logo" :width="100" style="cursor: pointer" />
    </v-toolbar-title>
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
  </v-app-bar>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'
import DxMenu from 'devextreme-vue/menu'
import logo from '@/assets/logo.svg'

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

    return {
      menu,
      showSubmenuModes,
      logo,
      showMenu,
      itemClick
    }
  }
})
</script>
