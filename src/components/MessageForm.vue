<script setup>
import { ref } from "vue"

const name = ref("")
const message = ref("")

const emit = defineEmits(["send-message"])
</script>

<template>
  <div class="fixed-bottom container">
    <div class="input-group my-3">
      <input type="text" class="form-control" placeholder="名前" v-model="name">
      <input type="text" class="form-control" placeholder="メッセージ" v-model="message">
      <button class="btn btn-primary" type="button" @click="$emit('send-message', [name, message])">
        <i class="bi bi-send"></i>
      </button>
    </div>
  </div>
</template>
