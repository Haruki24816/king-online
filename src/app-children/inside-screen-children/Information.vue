<script setup>
const props = defineProps({
  on: String
})
// メモ：部屋の名前省略
</script>

<template>
  <template v-if="on == 'bar'">
    <div class="text-center text-white">
      <div><strong>部屋の名前</strong></div>
      <div class="-font-small">0人・募集中</div>
    </div>
  </template>
  <template v-if="on == 'box'">
    <div class="text-white">
      <div class="text-center mt-2 mb-1"><img src="/src/assets/logo.svg" width="160"></div>
      <div class="text-center">部屋の名前</div>
      <h5 class="text-center">部屋の名前</h5>
      <div class="row row-cols-2 mt-3 mb-3 mx-4 g-0">
        <div class="col">参加人数</div>
        <div class="col text-end">0人</div>
        <div class="col">状況</div>
        <div class="col text-end">募集中</div>
      </div>
    </div>
  </template>
  <template v-if="on == 'offcanvas-header'">
    <img src="/src/assets/logo-white.svg" height="48">
    <h5 class="offcanvas-title ms-2" id="offcanvasLeftLabel">部屋の名前</h5>
    <div class="flex-grow-1"></div>
  </template>
  <template v-if="on == 'offcanvas-body'">
    <div class="row row-cols-2 gx-0 gy-1">
      <div class="col">参加人数</div>
      <div class="col text-end">0人</div>
      <div class="col">状況</div>
      <div class="col text-end">募集中</div>
    </div>
  </template>
</template>

<style scoped>
.-font-small {
  font-size: 12px;
}
</style>
