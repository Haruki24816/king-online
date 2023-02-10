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
  console.log("s0-error-unknown")
})

$socket.on("s0-enter-room", (data) => {
  console.log("s0-enter-room")
})

$socket.on("s0-dist-room-info", (data) => {
  console.log("s0-dist-room-info")
})

$socket.on("s0-dist-player-data", (data) => {
  console.log("s0-dist-player-data")
})

$socket.on("s0-error-no-room-id", () => {
  store0.value.failedEnterRoomReason = "存在しない部屋です"
})

$socket.on("s0-error-same-player-name", () => {
  store0.value.failedEnterRoomReason = "同じ名前のプレイヤーが入室しています"
})

$socket.on("s0-reconnect", () => {
  console.log("s0-reconnect")
})

$socket.on("s0-failed-reconnect", () => {
  console.log("s0-failed-reconnect")
})
</script>

<template></template>
