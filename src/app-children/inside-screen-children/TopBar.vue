<template>
  <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasLeft">
    <i class="bi bi-list fs-5"></i>
  </button>
  <div class="flex-grow-1 text-center text-white">
    <strong>部屋の名前</strong>
    <div class="-text-small">0人・募集中</div>
  </div>
  <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight">
    <i class="bi bi-chat-dots fs-5"></i>
  </button>
</template>

<style scoped>
.-text-small {
  font-size: 12px;
}
</style>
