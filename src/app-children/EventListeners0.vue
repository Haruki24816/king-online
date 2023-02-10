<script setup>
import { inject } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

$socket.on("connect", () => {
  store0.value.connection = true
})

$socket.on("disconnect", () => {
  store0.value.connection = false
})

$socket.on("s0-error-unknown", () => {
  store0.value.unknownErrorModal.show()
})

$socket.on("s0-enter-room", (data) => {
  store0.value.appMode = "inside"
  store0.value.roomId = data.room_id
  store0.value.playerId = data.player_id
  store0.value.enterModal.hide()
  store0.value.makeModal.hide()
})

$socket.on("s0-dist-room-info", (data) => {
  store0.value.roomName = data.room_info.room_name
  store0.value.playerNum = data.room_info.player_num
})

$socket.on("s0-dist-players-data", (data) => {
  store0.value.players = data.players
  console.log(data.players)
})

$socket.on("s0-error-no-room-id", () => {
  store0.value.failedEnterRoomReason = "存在しない部屋です"
  store0.value.entranceLock = false
})

$socket.on("s0-error-same-player-name", () => {
  store0.value.failedEnterRoomReason = "同じ名前のプレイヤーが入室しています"
  store0.value.entranceLock = false
})

$socket.on("s0-reconnect", () => {
  console.log("s0-reconnect")
})

$socket.on("s0-failed-reconnect", () => {
  console.log("s0-failed-reconnect")
})
</script>

<template></template>
