<script setup>
import ModalBase from "/src/base-components/ModalBase.vue"
import { inject, computed, ref } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

const roomId = ref("")
const playerName = ref("")

const isDisabled = computed(() => {
  return !(roomId.value.length == 8 &&
    1 <= playerName.value.length &&
    playerName.value.length <= 100 &&
    store0.value.connection &&
    !store0.value.entranceLock)
})

function enterRoom() {
  if (!isDisabled.value) {
    store0.value.entranceLock = true
    store0.value.failedEnterRoomReason = undefined
    $socket.emit("c0-enter-room", { "room_id": roomId.value, "player_name": playerName.value })
  } else if (roomId.value == "dev_mode") {
    $socket.disconnect()
    store0.value.entranceLock = true
    store0.value.failedEnterRoomReason = undefined
    store0.value.appMode = "inside"
    store0.value.roomId = "dev_mode"
    store0.value.playerId = 0
    store0.value.modals.enterRoom.hide()
    store0.value.modals.makeRoom.hide()
    store0.value.setUrlId("dev_mode")
    store0.value.players = [{ name: "player" }]
  }
}

const urlId = store0.value.getUrlId()
if (urlId != null && urlId.length == 8) {
  roomId.value = urlId
}
</script>

<template>
  <ModalBase name="enterRoom" title="部屋に入る" num="0">
    <div class="modal-body">
      <div class="alert alert-danger d-flex align-items-center" v-if="store0.failedEnterRoomReason != undefined">
        <i class="bi bi-exclamation-triangle-fill fs-4 me-3"></i>
        <div>{{ store0.failedEnterRoomReason }}</div>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="enterRoomId" placeholder="_" v-model="roomId"
          @keydown.enter="enterRoom">
        <label for="enterRoomId">部屋のID</label>
      </div>
      <div class="form-floating mb-3">
        <input type="text" class="form-control" id="enterRoomName" placeholder="_" v-model="playerName"
          @keydown.enter="enterRoom">
        <label for="enterRoomName">あなたの名前</label>
      </div>
      <div class="d-grid gap-2">
        <button :class="['btn', 'btn-primary', { 'disabled': isDisabled }]" @click="enterRoom">入室</button>
      </div>
    </div>
  </ModalBase>
</template>
