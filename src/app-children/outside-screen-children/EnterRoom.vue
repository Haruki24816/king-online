<script setup>
import { inject, computed, ref } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

const roomId = ref("")
const playerName = ref("")
const reason = ref("")
const alert = ref(false)

const buttonClass = computed(() => {
  if (roomId.value.length == 8 &&
    1 <= playerName.value.length &&
    playerName.value.length <= 100 &&
    store0.value.connection &&
    !store0.value.entranceLock) {
    return "btn btn-primary"
  } else {
    return "btn btn-primary disabled"
  }
})

function enterRoom() {
  store0.value.entranceLock = true
  alert.value = false
  $socket.emit("c0-enter-room", { "room_id": roomId, "player_name": playerName })
}

$socket.on("s0-failed-enter-room", (data) => {
  reason.value = data.reason
  alert.value = true
  store0.value.entranceLock = false
})
</script>

<template>
  <div class="alert alert-danger d-flex align-items-center" v-if="alert">
    <i class="bi bi-exclamation-triangle-fill fs-4 me-3"></i>
    <div>{{ reason }}</div>
  </div>
  <div class="form-floating mb-3">
    <input type="text" class="form-control" id="enterRoomId" placeholder="" v-model="roomId">
    <label for="enterRoomId">部屋のID</label>
  </div>
  <div class="form-floating mb-3">
    <input type="text" class="form-control" id="enterRoomName" placeholder="" v-model="playerName">
    <label for="enterRoomName">あなたの名前</label>
  </div>
  <div class="d-grid gap-2">
    <button :class="buttonClass" @click="enterRoom">入室</button>
  </div>
</template>
