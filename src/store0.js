import { ref } from "vue"

export const store0 = ref({
  appMode: "outside", // outside, inside
  outsideMode: "message", // splash, menu, message
  roomName: "きのこの山",
  roomInfo: {"項目1": "内容", "項目2": "内容"},
  disconnectionReason: "切断理由"
})
