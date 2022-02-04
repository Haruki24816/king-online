var socket = io();

socket.on("connect", function() {
  socket.emit("check_room_id", {"room_id": room_id});
  document.getElementById("connection_status").innerText = "ルームID確認中";
});

socket.on("kick", function(data) {
  document.getElementById("connection_status").innerText = "切断されました：" + data["message"];
});

socket.on("ask_player_name", function(data) {
  document.getElementById("connection_status").innerText = "接続中";
  document.getElementById("room_name").innerText = data["room_name"];
  document.getElementById("room_description").innerText ="募集中";
  document.getElementById("connection_status").classList.add("hidden");
  document.getElementById("header").classList.remove("hidden");
});
