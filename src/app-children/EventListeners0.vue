<script setup>
import { inject } from "vue"
import { store0 } from "/src/store0.js"

const $socket = inject("$socket")

$socket.on("connect", () => {
  store0.value.connection = true
})

$socket.on("disconnect", () => {
  store0.value.connection = false
})

$socket.on("s0-failed-make-room", (data) => {
  store0.failedMakeRoomReason.value = data.reason
  store0.failedMakeRoomAlert.value = true
  store0.value.entranceLock = false
})

$socket.on("s0-failed-enter-room", (data) => {
  store0.failedEnterRoomReason.value = data.reason
  store0.failedEnterRoomAlert.value = true
  store0.value.entranceLock = false
})
</script>
