<script setup>
import { ref, computed, inject, onMounted } from "vue"
import { Modal } from "bootstrap"

const $socket = inject("$socket")

const changeNameModalElement = ref()
const changeNameModal = ref()
const newName = ref("")

const isDisabled = computed(() => {
  return !(1 <= newName.value.length && newName.value.length <= 100)
})

onMounted(() => {
  changeNameModal.value = new Modal(changeNameModalElement.value)
})

function changeName() {
  if (!isDisabled.value) {
    $socket.emit("c0-change-name", { "new_name": newName.value })
    newName.value = ""
    changeNameModal.value.hide()
  }
}
</script>

<template>
  <div class="modal fade" id="changeNameModal" ref="changeNameModalElement" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="changeNameModalLabel">名前の変更</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <div class="form-floating">
            <input type="text" class="form-control" id="changeNameForm" placeholder="_" v-model="newName"
              @keydown.enter="changeName">
            <label for="changeNameForm">新しい名前</label>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">キャンセル</button>
          <button type="button" :class="['btn', 'btn-primary', { 'disabled': isDisabled }]" @click="changeName"
            data-bs-dismiss="modal">変更</button>
        </div>
      </div>
    </div>
  </div>
</template>
