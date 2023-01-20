<script setup>
import { store0 } from "./store0.js"
import SplashScreen from "./components/SplashScreen.vue"
import MessageScreen from "./components/MessageScreen.vue"
</script>

<template>
  <SplashScreen v-if="store0.screenNum == 0" />
  <!-- EntranceScreen / -->
  <!-- MainScreen / -->
  <MessageScreen v-if="store0.screenNum == 3" message="切断されました" description="理由テキスト" />
  <!-- InterruptionDisplay / -->
</template>
