import { ref } from "vue"

export const store0 = ref({
  appMode: "outside", // outside, inside
  outsideMode: "menu", // menu, message
  roomName: undefined,
  roomInfo: {},
  disconnectionReason: undefined,
  overlay: false,
  connection: false,
  entranceLock: false,
  failedEnterRoomReason: undefined
})
