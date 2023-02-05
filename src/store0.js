import { ref } from "vue"

export const store0 = ref({
  appMode: "outside", // outside, inside
  outsideMode: "menu", // menu, message
  roomName: "",
  roomInfo: {},
  disconnectionReason: "",
  overlay: false,
  connection: false,
  entranceLock: false
})
