<template>
  <DxDataGrid
    :data-source="users"
    key-expr="id"
    :show-borders="true"
    :allow-column-reordering="true"
    @row-inserting="addUser"
    @row-updating="updateRow"
  >
    <DxScrolling row-rendering-mode="virtual" />
    <DxPaging :page-size="10" />
    <DxHeaderFilter :visible="true" />
    <DxFilterPanel :visible="true" />
    <DxFilterBuilderPopup :position="filterBuilderPopupPosition" />
    <DxPager
      :visible="true"
      :allowed-page-sizes="pageSizes"
      display-mode="full"
      :show-page-size-selector="true"
      :show-info="true"
      :show-navigation-buttons="true"
    />
    <DxEditing :allow-updating="true" :allow-adding="true" mode="popup">
      <DxPopup :show-title="true" :width="700" :height="525" title="" />
      <DxForm>
        <DxItem :col-count="2" :col-span="2" item-type="group">
          <DxItem data-field="id" :visible="false" />
          <DxItem data-field="username" />
          <DxItem data-field="email" />
          <DxItem data-field="name" />
          <DxItem :validation-rules="validationRules.company" data-field="company" />
          <DxItem :validation-rules="validationRules.position" data-field="profile"> </DxItem>
        </DxItem>
      </DxForm>
    </DxEditing>
    <DxColumn data-field="id" />
    <DxColumn data-field="username" />
    <DxColumn data-field="email" />
    <DxColumn data-field="name" />
    <DxColumn data-field="company">
      <DxLookup :data-source="listCompany" display-expr="name" value-expr="id" />
    </DxColumn>
    <DxColumn data-field="profile">
      <DxLookup :data-source="listProfile" display-expr="name" value-expr="id" />
    </DxColumn>
  </DxDataGrid>

  <DxToast v-model:visible="isVisible" v-model:message="message" v-model:type="type" />
</template>
<script lang="ts">
import { defineComponent, ref } from 'vue'
import {
  DxDataGrid,
  DxScrolling,
  DxPager,
  DxPaging,
  DxEditing,
  DxPopup,
  DxForm,
  DxHeaderFilter,
  DxFilterPanel,
  DxFilterBuilderPopup,
  DxLookup,
  DxColumn
} from 'devextreme-vue/data-grid'
import { DxItem } from 'devextreme-vue/form'
import type { PositionConfig } from 'devextreme/animation/position'
import type { RowInsertedEvent, RowUpdatingEvent  } from 'devextreme/ui/data_grid'
import { DxToast } from 'devextreme-vue/toast'
import type { UserGrid, ProfileOut, CompanyOut } from '@/types/Administracao'
import apiService from '@/services/Apiservices'
import type { AxiosError } from 'axios'

export default defineComponent({
  name: 'DatagridUser',
  components: {
    DxDataGrid,
    DxScrolling,
    DxPaging,
    DxPager,
    DxEditing,
    DxPopup,
    DxForm,
    DxItem,
    DxColumn,
    DxFilterPanel,
    DxFilterBuilderPopup,
    DxLookup,
    DxHeaderFilter,
    DxToast
  },
  data() {
    const filterBuilderPopupPosition: PositionConfig = {
      of: window,
      at: 'top',
      my: 'top',
      offset: { y: 10 }
    }
    const validationRules = {
      position: [{ type: 'required', message: 'Position is required.' }],
      company: [{ type: 'required', message: 'Company is required.' }]
    }

    const listProfile: ProfileOut[] = []
    const listCompany: CompanyOut[] = []

    const isVisible = ref(false)
    const message = ref('')
    const type = ref('info')

    return {
      users: [] as Array<UserGrid>,
      pageSizes: [5, 10, 'all'],
      filterBuilderPopupPosition,
      validationRules,
      listProfile,
      listCompany,
      isVisible,
      message,
      type
    }
  },
  async created() {
    await this.getProfiles()
    await this.getUsers()
    await this.getCompany()
  },
  methods: {
    async getUsers() {
      const users = await apiService.getAllUser()
      this.users = users
    },
    async getProfiles() {
      try {
        const listProfile = await apiService.getProfile()
        this.listProfile = listProfile
      } catch (error) {
        console.error('Erro ao obter os perfis:', error)
      }
    },
    async getCompany() {
      try {
        const listCompany = await apiService.getCompany()
        this.listCompany = listCompany
      } catch (error) {
        console.error('Erro ao obter os company:', error)
      }
    },
    async addUser(e: RowInsertedEvent) {
      console.log(e)
      try {
        await apiService.addUser(e.data)
      } catch (e) {
        const error = e as AxiosError
        if (error.response?.status == 403) {
          const responseData = error.response.data as { detail: string }
          this.type = 'warning'
          this.message = responseData.detail
          this.isVisible = true
          setTimeout(()=>{ this.isVisible = false }, 3000)
        } else {
          this.type = 'error'
          this.message = 'Error ao cadastrar usuario'
          this.isVisible = true
          setTimeout(()=>{ this.isVisible = false }, 3000)
        }
      }
    },
    async updateRow(e: RowUpdatingEvent) {
      console.log(e)
      try {
        await apiService.updateUser(e.oldData.id, e.oldData)
      } catch (e) {
        const error = e as AxiosError
        if (error.response?.status == 403) {
          const responseData = error.response.data as { detail: string }
          this.type = 'warning'
          this.message = responseData.detail
          this.isVisible = true
          setTimeout(()=>{ this.isVisible = false }, 3000)
        } else {
          this.type = 'error'
          this.message = 'Error ao atualizar usuario'
          this.isVisible = true
          setTimeout(()=>{ this.isVisible = false }, 3000)
        }
      }
    }
  }
})
</script>
