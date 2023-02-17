<script setup>
import { onMounted } from "vue"
import { store0 } from "/src/store0.js"
import EnterRoom from "./outside-screen-children/EnterRoom.vue"
import MakeRoom from "./outside-screen-children/MakeRoom.vue"
import About from "./outside-screen-children/About.vue"

onMounted(() => {
  const urlId = store0.value.getUrlId()
  if (urlId != null && urlId.length == 8 && store0.value.outsideMode == "menu") {
    store0.value.modals.enterRoom.show()
  }
})

function reload() {
  location.reload()
}
</script>

<template>
  <div class="position-relative bg-dark -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center w-100">
      <img src="/src/assets/logo.svg" width="180">
      <template v-if="store0.outsideMode == 'menu'">
        <div class="mt-3"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#enterRoomModal">部屋に入る</button></div>
        <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#makeRoomModal">部屋を作る</button></div>
        <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#aboutModal">このサイトについて</button></div>
      </template>
      <template v-if="store0.outsideMode == 'message'">
        <h3 class="text-white mt-4">退室しました</h3>
        <p class="text-white">{{ store0.disconnectionReason }}</p>
        <button type="button" class="btn btn-dark" @click="reload">戻る</button>
      </template>
    </div>
  </div>
  <EnterRoom />
  <MakeRoom />
  <About />
</template>

<style scoped>
.-background {
  width: 100vw;
  height: 100vh;
}
</style>
