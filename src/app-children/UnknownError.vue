<script setup>
import { ref, onMounted } from "vue"
import { store0 } from "/src/store0.js"
import { Modal } from "bootstrap"

const unknownErrorModal = ref(null)

onMounted(() => {
  store0.value.unknownErrorModal = new Modal(unknownErrorModal.value)
})
</script>

<template>
  <div class="modal fade" id="unknownErrorModal" ref="unknownErrorModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="unknownErrorModalLabel">エラー</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          不明なエラーが発生しました
        </div>
      </div>
    </div>
  </div>
</template>
