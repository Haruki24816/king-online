<script setup>
import { store0 } from "./store0.js"
import SplashScreen from "./components/SplashScreen.vue"
import DisconnectScreen from "./components/DisconnectScreen.vue"
</script>

<template>
  <SplashScreen v-if="store0.screenNum == 0" />
  <!-- EntranceScreen / -->
  <!-- MainScreen / -->
  <DisconnectScreen v-if="store0.screenNum == 3" />
  <!-- InterruptionDisplay / -->
</template>
