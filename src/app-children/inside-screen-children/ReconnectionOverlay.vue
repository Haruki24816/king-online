<script setup>
import { store0 } from "/src/store0.js"
</script>

<template>
  <div class="position-fixed -overlay" v-if="store0.overlay">
    <div class="position-relative -box">
      <div class="position-absolute top-50 start-50 translate-middle">
        <div class="spinner-border -spinner"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.-overlay {
  width: 100vw;
  height: 100vh;
  background-color: #ffffff7f;
}

.-box {
  width: 100%;
  height: 100%;
}

.-spinner {
  width: 3rem;
  height: 3rem;
}
</style>
