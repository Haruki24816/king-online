<script setup>
import { store0 } from "/src/store0.js"
import EntranceMenu from "./outside-screen-children/EntranceMenu.vue"
import MessageDisplay from "./outside-screen-children/MessageDisplay.vue"
</script>

<template>
  <div class="position-relative bg-dark -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center">
      <img src="/src/assets/logo.svg" width="180">
      <EntranceMenu v-if="store0.outsideMode == 'menu'" />
      <MessageDisplay v-if="store0.outsideMode == 'message'" />
    </div>
  </div>
</template>

<style scoped>
.-background {
  width: 100vw;
  height: 100vh;
}
</style>
