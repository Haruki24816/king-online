<script setup>
import { inject } from "vue"
import { store0 } from "/src/store0.js"
import { store1 } from "/src/store1.js"

const $socket = inject("$socket")

$socket.on("connect", () => {
  store0.value.connection = true
  if (store0.value.overlay == true) {
    $socket.emit("c0-reconnect", {
      room_id: store0.value.roomId,
      player_id: store0.value.playerId
    })
  }
})

$socket.on("disconnect", () => {
  store0.value.connection = false
  if (store0.value.appMode == "inside") {
    store0.value.overlay = true
    setTimeout(() => {
      if (store0.value.overlay == true) {
        store0.value.appMode = "disconnection"
        store0.value.disconnectionReason = "接続を維持できなくなりました"
        $socket.disconnect()
      }
    }, 70000)
  }
})

$socket.on("s0-error-unknown", () => {
  store0.value.modals.unknownError.show()
})

$socket.on("s0-enter-room", (data) => {
  store0.value.appMode = "inside"
  store0.value.roomId = data.room_id
  store0.value.playerId = data.player_id
  store0.value.modals.enterRoom.hide()
  store0.value.modals.makeRoom.hide()
  store0.value.setUrlId(data.room_id)
})

$socket.on("s0-dist-room-info", (data) => {
  store0.value.roomName = data.room_info.room_name
  store0.value.playerNum = data.room_info.player_num
  store0.value.roomStatus = data.room_info.room_status
})

$socket.on("s0-dist-players-data", (data) => {
  store0.value.players = data.players
  store0.value.myName = data.players[store0.value.playerId].name
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
  store0.value.overlay = false
  store1.value.chatLog.push({
    "type": "info",
    "author": null,
    "content": "再接続しました",
    "timestamp": null
  })
})

$socket.on("s0-failed-reconnect", () => {
  store0.value.appMode = "disconnection"
  store0.value.disconnectionReason = "接続を維持できなくなりました"
  $socket.disconnect()
})

$socket.on("s0-no-owner", () => {
  store0.value.appMode = "disconnection"
  store0.value.disconnectionReason = "内閣総理大臣が欠けたため、憲法第70条により内閣総辞職となりました"
  $socket.disconnect()
  store0.value.deleteUrlId()
})

$socket.on("s0-finish", () => {
  store0.value.appMode = "disconnection"
  store0.value.disconnectionReason = "部屋は解散されました"
  $socket.disconnect()
  store0.value.deleteUrlId()
})

$socket.on("s0-kick", (data) => {
  store0.value.appMode = "disconnection"
  store0.value.disconnectionReason = "キックされました"
  if (data.reason != "") {
    store0.value.disconnectionReason += "：" + data.reason
  }
  $socket.disconnect()
})
</script>

<template></template>
