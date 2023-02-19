<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <div class="d-grid gap-2 m-3">
    <button class="btn btn-light" type="button" data-bs-toggle="modal" data-bs-target="#inviteModal">招待</button>
    <button class="btn btn-light" type="button" data-bs-toggle="modal" data-bs-target="#leaveModal">退室</button>
    <template v-if="store0.playerId == 0">
      <button class="btn btn-light" type="button" data-bs-toggle="modal" data-bs-target="#kickModal">キック</button>
    </template>
  </div>
</template>
