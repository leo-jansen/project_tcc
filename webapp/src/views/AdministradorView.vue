<template>
  <div class="container">
    <div class="col" id="content">
      <div class="card mr-4">
        <div class="card-body">
          <dataGridUser />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import dataGridUser from '@/components/DatagridUser.vue'

export default defineComponent({
  name: 'LoginView',
  components: { dataGridUser }
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
