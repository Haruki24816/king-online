<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <div class="text-white">
    <div class="text-center mt-2 mb-1"><img src="/src/assets/logo.svg" width="160"></div>
    <div class="text-center">部屋の名前</div>
    <h5 class="text-center mx-2">{{ store0.roomName }}</h5>
    <div class="row row-cols-2 mt-3 mb-3 mx-4 g-0">
      <div class="col">人数</div>
      <div class="col text-end">{{ store0.playerNum }}</div>
    </div>
  </div>
</template>
