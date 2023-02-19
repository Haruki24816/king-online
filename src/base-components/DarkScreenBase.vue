<template>
  <div class="position-relative bg-dark -background">
    <div class="position-absolute top-50 start-50 translate-middle text-center w-100">
      <div><img src="/src/assets/logo.svg" width="180"></div>
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.-background {
  width: 100vw;
  height: 100vh;
}
</style>
