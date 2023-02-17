<script setup>
import ModalBase from "/src/base-components/ModalBase.vue"
import { ref } from "vue"

const url = ref(location.href)

function copyUrl() {
  navigator.clipboard.writeText(location.href)
}
</script>

<template>
  <ModalBase name="invite" title="URLの共有" num="0">
    <div class="modal-body">
      <div class="input-group">
        <input type="text" class="form-control" readonly v-model="url">
        <button class="btn btn-primary" type="button" @click="copyUrl">コピー</button>
      </div>
    </div>
  </ModalBase>
</template>
