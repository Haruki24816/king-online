<script setup>
import { store1 } from "/src/store1.js"

const props = defineProps({ data: Object })
</script>

<template>
  <template v-if="data.type == 'message'">
    <div class="my-3">
      <div>
        <strong>{{ store1.getPlayerName(data.author) }}</strong>
        <span>&nbsp;</span>
        <small class="text-muted">{{ data.timestamp }}</small>
      </div>
      <div>
        {{ data.content }}
      </div>
    </div>
  </template>
  <template v-if="data.type == 'info'">
    <div class="alert alert-primary my-3">
      {{ data.content }}
    </div>
  </template>
</template>
