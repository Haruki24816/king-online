<script setup>
import { store0 } from "/src/store0.js"
import EntranceMenu from "./outside-screen-children/EntranceMenu.vue"
import MessageDisplay from "./outside-screen-children/MessageDisplay.vue"
</script>

<template>
  <div class="position-relative bg-dark -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center">
      <img src="/src/assets/logo.svg" width="180">
      <EntranceMenu v-if="store0.outsideMode == 'menu'" />
      <MessageDisplay v-if="store0.outsideMode == 'message'" />
    </div>
  </div>
  <div class="modal fade" id="XXX" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="XXXLabel">Modal title</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
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
