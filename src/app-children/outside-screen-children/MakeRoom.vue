<script setup>
import { inject, computed, ref } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

const roomName = ref("")
const ownerName = ref("")
const reason = ref("")
const alert = ref(false)

const buttonClass = computed(() => {
  if (1 <= roomName.value.length &&
    roomName.value.length <= 100 &&
    1 <= ownerName.value.length &&
    ownerName.value.length <= 100 &&
    store0.value.connection &&
    !store0.value.entranceLock) {
    return "btn btn-primary"
  } else {
    return "btn btn-primary disabled"
  }
})

function makeRoom() {
  store0.value.entranceLock = true
  alert.value = false
  $socket.emit("c0-make-room", { "room_name": roomName, "owner_name": ownerName })
}

$socket.on("s0-failed-make-room", (data) => {
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
    <input type="text" class="form-control" id="makeRoomName" placeholder="" v-model="roomName">
    <label for="makeRoomName">部屋の名前</label>
  </div>
  <div class="form-floating mb-3">
    <input type="text" class="form-control" id="makeRoomPlayerName" placeholder="" v-model="ownerName">
    <label for="makeRoomPlayerName">あなたの名前</label>
  </div>
  <div class="d-grid gap-2">
    <button :class="buttonClass" @click="makeRoom">作成</button>
  </div>
</template>
