<template>
  <div class="container">
    <div class="col" id="content">
      <div class="card mr-4">
        <div class="card-body">
          <DxDataGrid :data-source="users" key-expr="id" :show-borders="true">
            <DxScrolling row-rendering-mode="virtual" />
            <DxPaging :page-size="10" />
            <DxPager
              :visible="true"
              :allowed-page-sizes="pageSizes"
              display-mode="full"
              :show-page-size-selector="true"
              :show-info="true"
              :show-navigation-buttons="true"
            />
          </DxDataGrid>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { DxDataGrid, DxScrolling, DxPager, DxPaging } from 'devextreme-vue/data-grid'
import apiService from '@/services/Apiservices'

export default defineComponent({
  name: 'LoginView',
  components: { DxDataGrid, DxScrolling, DxPaging, DxPager },
  data() {
    let users: [] = []
    const pageSizes = [5, 10, 'all']
    return {
      users,
      pageSizes
    }
  },
  created() {
    this.getUsers()
  },
  methods: {
    async getUsers() {
      const users = await apiService.getAllUser()
      this.$data.users = users
    }
  }
})
</script>
<style>
.container {
  max-width: 100vw !important;
}

#content {
  margin-top: 40px;
  justify-content: center;
  align-items: center;
}
</style>
