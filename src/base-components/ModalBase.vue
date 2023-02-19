<script setup>
import { ref, onMounted } from "vue"
import { Modal } from "bootstrap"

import { store0 } from "/src/store0.js"
const stores = [store0]

const props = defineProps({
  "name": String,
  "title": String,
  "num": String
})
const modalElement = ref()

onMounted(() => {
  stores[props.num].value.modals[props.name] = new Modal(modalElement.value)
})
</script>

<template>
  <div class="modal fade" :id="name + 'Modal'" ref="modalElement" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" :id="name + 'ModalLabel'">{{ title }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <slot>
          <div class="modal-body">
            <p>モーダル内容</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">閉じる</button>
            <button type="button" class="btn btn-primary">実行</button>
          </div>
        </slot>
      </div>
    </div>
  </div>
</template>
