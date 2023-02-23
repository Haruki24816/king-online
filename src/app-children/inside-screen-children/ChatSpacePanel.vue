<script setup>
import { store1 } from "/src/store1.js"
import ChatContent from "./chat-space-panel-children/ChatContent.vue"
</script>

<template>
  <div class="d-flex flex-column align-items-stretch h-100 px-3">
    <div class="flex-grow-1 overflow-auto -overflow">
      <ChatContent v-for="data in store1.chatLog" :data="data" />
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control">
      <button class="btn btn-primary" type="button"><i class="bi bi-send"></i></button>
    </div>
  </div>
</template>

<style scoped>
.-overflow {
  height: 0;
}
</style>
