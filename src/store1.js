import { ref } from "vue"
import { store0 } from "/src/store0.js"

export const store1 = ref({
  chatLog: [],
  getPlayerName(playerId) {
    if (store0.value.players != undefined) {
      return store0.value.players[playerId].name
    }
  },
  getTimestamp() {
    const date = new Date()
    let hour = date.getHours()
    let minute = date.getMinutes()
    if (String(hour).length == 1) {
      hour = "0" + hour
    }
    if (String(minute).length == 1) {
      minute = "0" + minute
    }
    return hour + ":" + minute
  }
})
