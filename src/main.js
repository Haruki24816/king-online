import { createApp } from "vue"
import "./styles.scss"
import * as bootstrap from "bootstrap"
import "bootstrap-icons/font/bootstrap-icons.css"
import io from "socket.io-client"
import App from "./App.vue"

const app = createApp(App)
app.config.globalProperties.$socket = io()
app.provide("$socket", app.config.globalProperties.$socket)
app.mount("#app")
