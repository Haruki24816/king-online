<script setup>
import { store0 } from "/src/store0.js"
import EventListeners0 from "./app-children/EventListeners0.vue"
import EntranceScreen from "./app-children/EntranceScreen.vue"
import DisconnectionScreen from "./app-children/DisconnectionScreen.vue"
import InsideScreen from "./app-children/InsideScreen.vue"
import UnknownError from "./app-children/UnknownError.vue"
</script>

<template>
  <EventListeners0 />
  <EntranceScreen v-if="store0.appMode == 'entrance'" />
  <DisconnectionScreen v-if="store0.appMode == 'disconnection'" />
  <InsideScreen v-if="store0.appMode == 'inside'" />
  <UnknownError />
</template>
