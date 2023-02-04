<script setup>
import { store0 } from "/src/store0.js"
import EnterRoom from "./outside-screen-children/EnterRoom.vue"
import MakeRoom from "./outside-screen-children/MakeRoom.vue"
import About from "./outside-screen-children/About.vue"
</script>

<template>
  <div class="position-relative bg-dark -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center">
      <img src="/src/assets/logo.svg" width="180">
      <template v-if="store0.outsideMode == 'menu'">
        <div class="mt-3"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#enter">部屋に入る</button></div>
        <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#make">部屋を作る</button></div>
        <div class="mt-1"><button type="button" class="btn btn-dark" data-bs-toggle="modal"
            data-bs-target="#about">このサイトについて</button></div>
      </template>
      <template v-if="store0.outsideMode == 'message'">
        <h3 class="text-white mt-4">退室しました</h3>
        <p class="text-white">{{ store0.disconnectionReason }}</p>
        <button type="button" class="btn btn-dark">戻る</button>
      </template>
    </div>
  </div>
  <div class="modal fade" id="enter" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="enterLabel">部屋に入る</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <EnterRoom />
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="make" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="makeLabel">部屋を作る</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <MakeRoom />
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="about" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="aboutLabel">このサイトについて</h5>
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
