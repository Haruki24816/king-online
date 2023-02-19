<script setup>
import { store0 } from "/src/store0.js"
import DarkScreenBase from "/src/base-components/DarkScreenBase.vue"

function reload() {
  location.reload()
}
</script>

<template>
  <DarkScreenBase>
    <h3 class="text-white mt-4">退室しました</h3>
    <p class="text-white">{{ store0.disconnectionReason }}</p>
    <button type="button" class="btn btn-dark" @click="reload">戻る</button>
  </DarkScreenBase>
</template>
