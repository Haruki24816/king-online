<script setup>
import { store1 } from "/src/store1.js"
import { ref, inject, computed } from "vue"
import ChatContent from "./chat-space-panel-children/ChatContent.vue"

const $socket = inject("$socket")
const message = ref("")

const isDisabled = computed(() => {
  return !(1 <= message.value.length && message.value.length <= 100)
})

function send() {
  if (!isDisabled.value) {
    $socket.emit("c1-message", { "message": message.value })
    message.value = ""
  }
}
</script>

<template>
  <div class="d-flex flex-column align-items-stretch h-100 px-3">
    <div class="flex-grow-1 overflow-auto -overflow">
      <ChatContent v-for="data in store1.chatLog" :data="data" />
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" v-model="message" @keydown.enter="send">
      <button :class="['btn', 'btn-primary', { 'disabled': isDisabled }]" type="button" @click="send">
        <i class="bi bi-send"></i>
      </button>
    </div>
  </div>
</template>

<style scoped>
.-overflow {
  height: 0;
}
</style>
