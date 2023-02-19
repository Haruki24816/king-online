<script setup>
import { onMounted } from "vue"
import { store0 } from "/src/store0.js"
import DarkScreenBase from "/src/base-components/DarkScreenBase.vue"
import EnterRoom from "./entrance-screen-children/EnterRoom.vue"
import MakeRoom from "./entrance-screen-children/MakeRoom.vue"
import About from "./entrance-screen-children/About.vue"

onMounted(() => {
  const urlId = store0.value.getUrlId()
  if (urlId != null && urlId.length == 8) {
    store0.value.modals.enterRoom.show()
  }
})
</script>

<template>
  <DarkScreenBase>
    <div class="mt-3"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
        data-bs-target="#enterRoomModal">部屋に入る</button></div>
    <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
        data-bs-target="#makeRoomModal">部屋を作る</button></div>
    <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
        data-bs-target="#aboutModal">このサイトについて</button></div>
  </DarkScreenBase>
  <EnterRoom />
  <MakeRoom />
  <About />
</template>
