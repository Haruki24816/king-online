<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#gameMenuOffcanvas">
    <i class="bi bi-list fs-5"></i>
  </button>
  <div class="flex-grow-1 text-center text-white text-truncate">
    <strong>{{ store0.roomName }}</strong>
    <div class="-text-small">
      {{ store0.playerNum }}人
    </div>
  </div>
  <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#chatSpaceOffcanvas">
    <i class="bi bi-chat-dots fs-5"></i>
  </button>
</template>

<style scoped>
.-text-small {
  font-size: 12px;
}
</style>
