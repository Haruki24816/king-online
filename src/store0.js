import { ref } from "vue"

export const store0 = ref({
  appMode: "outside", // outside, inside
  outsideMode: "menu", // menu, message
  roomName: undefined,
  disconnectionReason: undefined,
  overlay: false,
  connection: false,
  entranceLock: false,
  failedEnterRoomReason: undefined,
  roomId: undefined,
  playerId: undefined,
  players: undefined,
  playerNum: undefined,
  enterModal: undefined,
  makeModal: undefined
})
