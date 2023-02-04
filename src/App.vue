<script setup>
import { store0 } from "/src/store0.js"
import OutsideScreen from "./app-children/OutsideScreen.vue"
import InsideScreen from "./app-children/InsideScreen.vue"
</script>

<template>
  <OutsideScreen v-if="store0.appMode == 'outside'" />
  <InsideScreen v-if="store0.appMode == 'inside'" />
</template>
