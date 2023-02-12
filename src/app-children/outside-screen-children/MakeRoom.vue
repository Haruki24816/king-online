<script setup>
import { inject, computed, ref } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

const roomName = ref("")
const ownerName = ref("")

const isDisabled = computed(() => {
  return !(1 <= roomName.value.length &&
    roomName.value.length <= 100 &&
    1 <= ownerName.value.length &&
    ownerName.value.length <= 100 &&
    store0.value.connection &&
    !store0.value.entranceLock)
})

function makeRoom() {
  store0.value.entranceLock = true
  $socket.emit("c0-make-room", { "room_name": roomName.value, "owner_name": ownerName.value })
}
</script>

<template>
  <div class="form-floating mb-3">
    <input type="text" class="form-control" id="makeRoomName" placeholder="" v-model="roomName">
    <label for="makeRoomName">部屋の名前</label>
  </div>
  <div class="form-floating mb-3">
    <input type="text" class="form-control" id="makeRoomPlayerName" placeholder="" v-model="ownerName">
    <label for="makeRoomPlayerName">あなたの名前</label>
  </div>
  <div class="d-grid gap-2">
    <button :class="['btn', 'btn-primary', { 'disabled': isDisabled }]" @click="makeRoom">作成</button>
  </div>
</template>
