<script setup>
import { inject } from "vue"

const $socket = inject("$socket")

function leave() {
  $socket.emit("c0-leave")
  const url = new URL(location)
  url.searchParams.delete("id")
  history.replaceState(null, null, url.toString())
  location.reload()
}
</script>

<template>
  <div class="modal fade" id="leaveModal" ref="leaveModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="leaveModalLabel">確認</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          この部屋から退室しますか？
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">キャンセル</button>
          <button type="button" class="btn btn-primary" @click="leave">退室</button>
        </div>
      </div>
    </div>
  </div>
</template>
