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
  makeModal: undefined,
  unknownErrorModal: undefined,
  modals: {},
  getUrlId() {
    const url = new URL(location)
    return url.searchParams.get("id")
  },
  setUrlId(urlId) {
    const url = new URL(location)
    url.searchParams.set("id", urlId)
    history.replaceState(null, null, url.toString())
  },
  deleteUrlId() {
    const url = new URL(location)
    url.searchParams.delete("id")
    history.replaceState(null, null, url.toString())
  }
})
