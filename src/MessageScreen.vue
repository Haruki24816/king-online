<script setup>
import ColorScreen from "./ColorScreen.vue"

const props = defineProps({
  message: String,
  description: String
})
</script>

<template>
  <ColorScreen>
    <h3 class="text-white mt-4">{{ message }}</h3>
    <p class="text-white">{{ description }}</p>
    <a href="#" class="text-white">エントランスへ</a>
  </ColorScreen>
</template>
