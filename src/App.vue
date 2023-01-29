<script setup>
import { store0 } from "/src/store0.js"
import SplashScreen from "./app-children/SplashScreen.vue"
import EntranceScreen from "./app-children/EntranceScreen.vue"
import MainScreen from "./app-children/MainScreen.vue"
import DisconnectScreen from "./app-children/DisconnectScreen.vue"
</script>

<template>
  <SplashScreen v-if="store0.screenNum == 0" />
  <EntranceScreen v-if="store0.screenNum == 1" />
  <MainScreen v-if="store0.screenNum == 2" />
  <DisconnectScreen v-if="store0.screenNum == 3" />
  <!-- InterruptionDisplay / -->
</template>
