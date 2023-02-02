<script setup>
import { ref } from "vue"
import OutsideScreen from "./app-children/OutsideScreen.vue"
import InsideScreen from "./app-children/InsideScreen.vue"

const num = ref(0)
</script>

<template>
  <OutsideScreen v-if="num == 0" />
  <InsideScreen v-if="num == 1" />
</template>
