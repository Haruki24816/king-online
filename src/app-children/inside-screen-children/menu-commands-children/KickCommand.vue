<script setup>
import { ref, computed } from "vue"
import { store0 } from "/src/store0.js"
import ModalBase from "/src/base-components/ModalBase.vue"
import { inject } from "vue"

const $socket = inject("$socket")

const reason = ref("")
const playerId = ref(0)

const isDisabled = computed(() => {
  return playerId.value == 0
})

function kick() {
  $socket.emit("c0-kick", { "player_id": playerId.value, "reason": reason.value })
  playerId.value = 0
  reason.value = ""
}
</script>

<template>
  <ModalBase name="kick" title="キック" num="0">
    <div class="modal-body">
      <select class="form-select mb-3" v-model="playerId">
        <option :value="num" v-for="(data, num) in store0.players">
          {{ num != 0 ? data.name : "プレイヤーを選択してください" }}
        </option>
      </select>
      <div class="form-floating">
        <input type="text" class="form-control" id="kickReason" placeholder="_" v-model="reason">
        <label for="kickReason">キックする理由</label>
      </div>
    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">キャンセル</button>
      <button type="button" :class="['btn', 'btn-primary', { 'disabled': isDisabled }]" data-bs-dismiss="modal"
        @click="kick">キック</button>
    </div>
  </ModalBase>
</template>
