<script setup>
const props = defineProps({
  author: String,
  timestamp: String,
  content: String
})
</script>

<template>
  <p>
    <span class="text-muted">{{ timestamp }}&nbsp;</span>
    <strong>{{ author }} </strong>
    {{ content }}
  </p>
</template>
