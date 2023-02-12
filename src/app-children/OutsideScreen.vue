<script setup>
import { ref, onMounted } from "vue"
import { store0 } from "/src/store0.js"
import { Modal } from "bootstrap"
import EnterRoom from "./outside-screen-children/EnterRoom.vue"
import MakeRoom from "./outside-screen-children/MakeRoom.vue"
import About from "./outside-screen-children/About.vue"

const enterModal = ref(null)
const makeModal = ref(null)

onMounted(() => {
  store0.value.enterModal = new Modal(enterModal.value)
  store0.value.makeModal = new Modal(makeModal.value)
  const param = (new URL(location)).searchParams.get("id")
  if (param != null && param.length == 8) {
    store0.value.enterModal.show()
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
            data-bs-target="#enterModal">部屋に入る</button></div>
        <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#makeModal">部屋を作る</button></div>
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
  <div class="modal fade" id="enterModal" ref="enterModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="enterModalLabel">部屋に入る</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <EnterRoom />
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="makeModal" ref="makeModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="makeModalLabel">部屋を作る</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <MakeRoom />
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="aboutModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="aboutModalLabel">このサイトについて</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <About />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.-background {
  width: 100vw;
  height: 100vh;
}
</style>
