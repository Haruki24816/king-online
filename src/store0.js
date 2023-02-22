import { ref } from "vue"

export const store0 = ref({
  appMode: "entrance", // entrance, disconnection, inside
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
  modals: {},
  roomStatus: "waiting", // waiting, gaming
  myName: undefined,
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
  },
  playerNames() {
    const playerNames = {}
    for (const num in this.players) {
      const data = this.players[num]
      if (data.status == "left") {
        continue
      }
      playerNames[data.name] = num
    }
    return playerNames
  }
})
