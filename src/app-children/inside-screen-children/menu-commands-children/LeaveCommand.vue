<script setup>
import ModalBase from "/src/base-components/ModalBase.vue"
import { inject } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

function leave() {
  $socket.emit("c0-leave")
  store0.value.deleteUrlId()
  location.reload()
}
</script>

<template>
  <ModalBase name="leave" title="確認" num="0">
    <div class="modal-body">
      この部屋から退室しますか？
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">キャンセル</button>
      <button type="button" class="btn btn-primary" @click="leave">退室</button>
    </div>
  </ModalBase>
</template>
