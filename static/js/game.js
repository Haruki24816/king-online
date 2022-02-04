function add_log(message) {
  let element = document.getElementById("log");
  let child = document.createElement("li");
  child.textContent = message;
  element.prepend(child);
}

function send_message() {
  let element = document.getElementById("textbox");
  let message = element.value;
  if (message == "") {
    return;
  }
  socket.emit("message", {"message": message});
  element.value = "";
}

var socket = io();

socket.on("connect", function() {
  socket.emit("join", {"game_id": game_id});
  add_log("接続");
});

socket.on("message", function(data) {
  add_log(data["message"]);
});

let textbox_element = document.getElementById("textbox");
textbox_element.addEventListener("keypress", function(e) {
  if (e.keyCode === 13) {
    send_message();
  }
});

let button_element = document.getElementById("button");
button_element.addEventListener("click", send_message);
