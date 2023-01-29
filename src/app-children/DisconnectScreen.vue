<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <div class="bg-primary position-relative -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center w-100 px-2">
      <img src="/src/assets/symbol.svg" class="-image">
      <h3 class="text-white mt-4">{{ store0.disconnectMessage }}</h3>
      <p class="text-white">{{ store0.disconnectDescription }}</p>
      <button class="btn btn-link text-white">エントランスへ</button>
    </div>
  </div>
</template>

<style scoped>
.-background {
  width: 100vw;
  height: 100vh;
}

.-image {
  width: 100px;
}
</style>
