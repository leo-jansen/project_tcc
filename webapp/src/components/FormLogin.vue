<template>
  <div class="mx-5">
    <v-card class="elevation-1 mx-auto mt-10" max-width="600">
      <v-card-text>
        <form action="your-action" @submit="handleSubmit">
          <DxForm
            v-model:form-data="loginData"
            :read-only="false"
            @initialized="saveFormInstance"
            :show-colon-after-label="true"
            :show-validation-summary="true"
            validation-group="customerData"
          >
            <DxSimpleItem data-field="Email" :editor-options="emailEditorOptions">
              <DxRequiredRule message="Email is required" />
              <DxEmailRule message="Email is invalid" />
              <DxAsyncRule
                :validation-callback="asyncValidation"
                message="Email is already registered"
              />
            </DxSimpleItem>
            <DxSimpleItem :editor-options="passwordEditorOptions" data-field="Password">
              <DxRequiredRule message="Password is required" />
            </DxSimpleItem>
          </DxForm>
        </form>
      </v-card-text>
      <v-card-actions class="justify-center">
        <DxGroupItem css-class="buttons-group" :col-count-by-screen="colCountByScreen">
          <DxButtonItem :button-options="registerButtonOptions" />
          <DxButtonItem :button-options="resetButtonOptions" name="Reset" />
        </DxGroupItem>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import DxForm, {
  DxSimpleItem,
  DxRequiredRule,
  DxEmailRule,
  DxAsyncRule,
  DxGroupItem,
  DxButtonItem
} from 'devextreme-vue/form'
import Validator from 'devextreme/ui/validator'

export default defineComponent({
  name: 'form-login',
  components: {
    DxForm,
    DxSimpleItem,
    DxRequiredRule,
    DxEmailRule,
    DxAsyncRule,
    DxGroupItem,
    DxButtonItem
  },
  setup() {
    const loginData = {
      Email: '',
      Password: ''
    }
    const formInstance = ref<DxForm | null>(null)
    const emailEditorOptions = ref({
      valueChangeEvent: 'keyup'
    })

    function asyncValidation(params: { value: any }) {
      return sendRequest(params.value)
    }

    function handleSubmit(e: Event) {
      e.preventDefault()
    }

    function saveFormInstance(e: { component: DxForm }) {
      formInstance.value = e.component
    }

    const sendRequest = function (value: string) {
      const invalidEmail = 'test@dx-email.com'
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve(value !== invalidEmail)
        }, 1000)
      })
    }

    const passwordEditorOptions = ref({
      mode: 'password',
      valueChangeEvent: 'keyup',
      onValueChanged: () => {
        const editor = formInstance.value.getEditor('ConfirmPassword')
        if (editor.option('value')) {
          const instance = Validator.getInstance(editor.element()) as Validator
          instance.validate()
        }
      },
      buttons: [
        {
          name: 'password',
          location: 'after',
          options: {
            icon: 'eyeopen',
            stylingMode: 'text',
            onClick: () => changePasswordMode('Password')
          }
        }
      ]
    })

    function changePasswordMode(name: string) {
      const editor = formInstance.value.getEditor(name)
      editor.option('mode', editor.option('mode') === 'text' ? 'password' : 'text')
    }

    const colCountByScreen = ref({ xs: 2, sm: 2, md: 2, lg: 2 })
    const registerButtonOptions = ref({
      text: 'Register',
      type: 'default',
      width: '120px',
      useSubmitBehavior: true
    })
    const resetButtonOptions = ref({
      icon: 'refresh',
      text: 'Reset',
      width: '120px',
      onClick: () => {
        formInstance.value.reset()
      }
    })

    return {
      handleSubmit,
      asyncValidation,
      emailEditorOptions,
      loginData,
      saveFormInstance,
      passwordEditorOptions,
      colCountByScreen,
      registerButtonOptions,
      resetButtonOptions
    }
  }
})
</script>
