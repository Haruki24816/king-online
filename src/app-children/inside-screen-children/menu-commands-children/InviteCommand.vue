<script setup>
import { ref } from "vue"

const url = ref(location.href)

function copyUrl() {
  navigator.clipboard.writeText(location.href)
}
</script>

<template>
  <div class="modal fade" id="inviteModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="inviteModalLabel">URLの共有</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <div class="input-group">
            <input type="text" class="form-control" readonly v-model="url">
            <button class="btn btn-primary" type="button" @click="copyUrl">コピー</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
