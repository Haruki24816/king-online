<script setup>
import { store0 } from "/src/store0.js"
import EventListeners0 from "./app-children/EventListeners0.vue"
import OutsideScreen from "./app-children/OutsideScreen.vue"
import InsideScreen from "./app-children/InsideScreen.vue"
import ErrorModal from "./app-children/ErrorModal.vue"
</script>

<template>
  <EventListeners0 />
  <OutsideScreen v-if="store0.appMode == 'outside'" />
  <InsideScreen v-if="store0.appMode == 'inside'" />
  <ErrorModal />
</template>
