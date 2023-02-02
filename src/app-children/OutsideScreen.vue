<script setup>
import { ref } from "vue"
import EntranceMenu from "./outside-screen-children/EntranceMenu.vue"
import MessageDisplay from "./outside-screen-children/MessageDisplay.vue"

const num = ref(0)
</script>

<template>
  <div class="position-relative bg-dark -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center">
      <img src="/src/assets/logo.svg" width="180">
      <EntranceMenu v-if="num == 1" />
      <MessageDisplay v-if="num == 2" />
    </div>
  </div>
</template>

<style scoped>
.-background {
  width: 100vw;
  height: 100vh;
}
</style>
