<script setup>
import { inject, computed, ref } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

const roomId = ref("")
const playerName = ref("")

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
  $socket.emit("c0-enter-room", { "room_id": roomId, "player_name": playerName })
}
</script>

<template>
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
