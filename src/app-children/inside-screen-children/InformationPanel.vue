<script setup>
import { computed } from "vue"
import { store0 } from "/src/store0.js"

const status = computed(() => {
  if (store0.value.roomStatus == "waiting") {
    return "待機中"
  }
  if (store0.value.roomStatus == "gaming") {
    return "対戦中"
  }
})
</script>

<template>
  <div class="text-white">
    <div class="text-center mt-2 mb-1"><img src="/src/assets/logo.svg" width="160"></div>
    <div class="text-center mx-2">{{ store0.myName }} としてログイン</div>
    <h5 class="text-center mx-2">{{ store0.roomName }}</h5>
    <div class="row row-cols-2 mt-3 mb-3 mx-4 g-0">
      <div class="col">現在</div>
      <div class="col text-end">{{ status }}</div>
      <div class="col">人数</div>
      <div class="col text-end">{{ store0.playerNum }}人</div>
    </div>
  </div>
</template>
