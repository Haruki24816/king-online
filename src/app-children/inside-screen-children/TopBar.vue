<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasLeft">
    <i class="bi bi-list fs-5"></i>
  </button>
  <div class="flex-grow-1 text-center text-white text-truncate">
    <strong>{{ store0.roomName }}</strong>
    <ul class="list-inline m-0 -text-small">
      <li class="list-inline-item" v-for="value in store0.roomInfo">{{ value }}</li>
    </ul>
  </div>
  <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight">
    <i class="bi bi-chat-dots fs-5"></i>
  </button>
</template>

<style scoped>
.-text-small {
  font-size: 12px;
}
</style>
