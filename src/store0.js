import { ref } from "vue"

export const store0 = ref({
  appMode: "outside", // outside, inside
  outsideMode: "splash", // splash, menu, message
  roomName: "",
  roomInfo: {},
  disconnectionReason: ""
})
