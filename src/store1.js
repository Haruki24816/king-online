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
    const hour = date.getHours()
    const minute = date.getMinutes()
    return hour + ":" + minute
  }
})
