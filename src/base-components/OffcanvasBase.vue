<script setup>
import { ref } from "vue"

const props = defineProps({
  "end": Boolean,
  "name": String,
  "title": String,
  "width": String
})
const styleObject = ref({})

if (props.width != undefined) {
  styleObject.value.maxWidth = props.width
}
</script>

<template>
  <div :class="[end ? 'offcanvas-end' : 'offcanvas-start', 'offcanvas']" tabindex="-1" :id="name + 'Offcanvas'"
    :style="styleObject">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" :id="name + 'OffcanvasLabel'">{{ title }}</h5>
      <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
      <slot></slot>
    </div>
  </div>
</template>
