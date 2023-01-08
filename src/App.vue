<script setup>
import { ref } from "vue"
import { io } from "socket.io-client"
import Message from "./components/Message.vue"
import MessageForm from "./components/MessageForm.vue"

const socket = io()
const log = ref([])

socket.on("connect", () => {
  log.value.push(["[システム]", getTimestamp(), "接続"])
})

socket.on("disconnect", () => {
  log.value.push(["[システム]", getTimestamp(), "切断"])
})

socket.on("message", (data) => {
  log.value.push([data[0], getTimestamp(), data[1]])
})

function sendMessage(name, content) {
  socket.emit("message", [name, content])
}

function getTimestamp() {
  const dd = new Date()
  const hh = dd.getHours()
  const mm = dd.getMinutes()
  const ss = dd.getSeconds()
  return hh + ":" + mm + ":" + ss
}
</script>

<template>
  <div class="container">
    <h1 class="my-4">適当チャット</h1>
    <Message v-for="message in log" :author="message[0]" :timestamp="message[1]" :content="message[2]" />
  </div>
  <MessageForm @send-message="sendMessage($event[0], $event[1])" />
</template>
