<script setup>
const props = defineProps({
  header: Boolean
})
</script>

<template>
  <div v-if="header">チャットスペース</div>
  <div>チャットスペース</div>
</template>
