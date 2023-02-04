<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <h3 class="text-white mt-4">退室しました</h3>
  <p class="text-white">{{ store0.disconnectionReason }}</p>
  <button type="button" class="btn btn-dark">戻る</button>
</template>
