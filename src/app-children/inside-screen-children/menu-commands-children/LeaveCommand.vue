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
      <template v-if="store0.playerId == 0">この部屋を解散します。本当によろしいですか？</template>
      <template v-else-if="store0.roomStatus == 'gaming'">あなたが退室するとゲームは中断されます。この部屋から退室しますか？</template>
      <template v-else>この部屋から退室しますか？</template>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">キャンセル</button>
      <button v-if="store0.playerId == 0" type="button" class="btn btn-danger" @click="leave">解散</button>
      <button v-else-if="store0.roomStatus == 'gaming'" type="button" class="btn btn-danger" @click="leave">退室</button>
      <button v-else type="button" class="btn btn-primary" @click="leave">退室</button>
    </div>
  </ModalBase>
</template>
