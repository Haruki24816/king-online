<script setup>
import { ref, onMounted } from "vue"
import { store0 } from "/src/store0.js"
import { Modal } from "bootstrap"

const errorModal = ref(null)

onMounted(() => {
  store0.value.errorModal = new Modal(errorModal.value)
})
</script>

<template>
  <div class="modal fade" id="errorModal" ref="errorModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="errorModalLabel">エラー</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          不明なエラーが発生しました
        </div>
      </div>
    </div>
  </div>
</template>
