<script setup>
import ComeRoom from "./entrance-screen-children/ComeRoom.vue"
import MakeRoom from "./entrance-screen-children/MakeRoom.vue"
import AboutApp from "./entrance-screen-children/AboutApp.vue"
</script>

<template>
  <div class="container -content">
    <div class="text-center my-5">
      <img src="../assets/logo.svg" class="-image">
    </div>
    <div class="accordion" id="entranceAccordion">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapseOne">
            <i class="bi bi-door-open-fill fs-4 me-2"></i>
            部屋に入る
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#entranceAccordion">
          <div class="accordion-body">
            <ComeRoom />
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapseTwo">
            <i class="bi bi-plus-square-fill fs-4 me-2"></i>
            部屋を作る
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#entranceAccordion">
          <div class="accordion-body">
            <MakeRoom />
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingThree">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapseThree">
            <i class="bi bi-file-text-fill fs-4 me-2"></i>
            King Online について
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#entranceAccordion">
          <div class="accordion-body">
            <AboutApp />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.-content {
  max-width: 400px;
}

.-image {
  width: 100%;
  max-width: 300px;
}
</style>
