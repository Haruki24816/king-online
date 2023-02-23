import { ref } from "vue"
import { store0 } from "/src/store0.js"

export const store1 = ref({
  chatLog: [
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "info", "author": null, "content": "インフォメーション", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 },
    { "type": "message", "author": 0, "content": "メッセージ", "timestamp": 0 }
  ],
  getPlayerName(playerId) {
    if (store0.value.players != undefined) {
      return store0.value.players[playerId].name
    }
  },
  getTimeString(timestamp) {
    const dateTime = new Date(timestamp * 1000)
    return dateTime.toLocaleTimeString().slice(0, 4)
  }
})
