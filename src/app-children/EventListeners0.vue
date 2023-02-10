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

$socket.on("s0-enter-room", (data) => {
  console.log("s0-enter-room")
})

$socket.on("s0-failed-make-room", (data) => {
  store0.failedMakeRoomReason.value = data.reason
  store0.failedMakeRoomAlert.value = true
  store0.value.entranceLock = false
})

$socket.on("s0-failed-enter-room", (data) => {
  store0.failedEnterRoomReason.value = data.reason
  store0.failedEnterRoomAlert.value = true
  store0.value.entranceLock = false
})

$socket.on("s0-room-info", (data) => {
  console.log("s0-room-info")
})

$socket.on("s0-player-data", (data) => {
  console.log("s0-player-data")
})

$socket.on("s0-reconnect", () => {
  console.log("s0-reconnect")
})

$socket.on("s0-failed-reconnect", () => {
  console.log("s0-failed-reconnect")
})
</script>

<template></template>
