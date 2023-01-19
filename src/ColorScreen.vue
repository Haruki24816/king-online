<template>
  <div class="bg-primary position-relative -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center -content">
      <div>
        <img src="./logo.svg" class="-image">
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<style>
.-background {
  width: 100vw;
  height: 100vh;
}

.-content {
  width: 90%;
  max-width: 400px;
}

.-image {
  width: 100px;
}
</style>
