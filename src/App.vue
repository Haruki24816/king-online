<script setup>
import { inject } from "vue"
import { store0 } from "/src/store0.js"
import OutsideScreen from "./app-children/OutsideScreen.vue"
import InsideScreen from "./app-children/InsideScreen.vue"

const $socket = inject("$socket")

$socket.on("connect", () => {
  store0.value.connection = true
})

$socket.on("disconnect", () => {
  store0.value.connection = false
})
</script>

<template>
  <OutsideScreen v-if="store0.appMode == 'outside'" />
  <InsideScreen v-if="store0.appMode == 'inside'" />
</template>
