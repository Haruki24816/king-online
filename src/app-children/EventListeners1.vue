<script setup>
import { inject } from "vue"
import { store1 } from "/src/store1.js"

const $socket = inject("$socket")

$socket.on("s1-message", (data) => {
  store1.value.chatLog.push({
    "type": "message",
    "author": data.player_id,
    "content": data.message,
    "timestamp": store1.value.getTimestamp()
  })
})

$socket.on("s1-join", (data) => {
  store1.value.chatLog.push({
    "type": "info",
    "author": null,
    "content": store1.value.getPlayerName(data.player_id) + " が入室しました",
    "timestamp": null
  })
})

$socket.on("s1-leave", (data) => {
  store1.value.chatLog.push({
    "type": "info",
    "author": null,
    "content": store1.value.getPlayerName(data.player_id) + " が退室しました",
    "timestamp": null
  })
})

$socket.on("s1-kick", (data) => {
  store1.value.chatLog.push({
    "type": "info",
    "author": null,
    "content": store1.value.getPlayerName(data.player_id) + " がキックされました",
    "timestamp": null
  })
})
</script>

<template></template>
