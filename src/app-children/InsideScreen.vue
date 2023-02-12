<script setup>
import ReconnectionOverlay from "./inside-screen-children/ReconnectionOverlay.vue"
import TopBar from "./inside-screen-children/TopBar.vue"
import InformationPanel from "./inside-screen-children/InformationPanel.vue"
import MenuPanel from "./inside-screen-children/MenuPanel.vue"
import GameDisplayPanel from "./inside-screen-children/GameDisplayPanel.vue"
import GameCommandPanel from "./inside-screen-children/GameCommandPanel.vue"
import ChatSpacePanel from "./inside-screen-children/ChatSpacePanel.vue"
import MenuCommands from "./inside-screen-children/MenuCommands.vue"
</script>

<template>
  <ReconnectionOverlay />
  <div class="d-flex flex-column -background">
    <div class="d-flex d-lg-none align-items-center container-fluid bg-dark p-1">
      <TopBar />
    </div>
    <div class="flex-grow-1 d-flex align-items-stretch container">
      <div class="d-none d-lg-flex flex-column align-items-stretch my-3 me-3 -left-box">
        <div class="bg-dark rounded mb-3">
          <InformationPanel />
        </div>
        <div class="bg-white rounded-top border-bottom text-center p-2">
          ゲームメニュー
        </div>
        <div class="flex-grow-1 bg-white rounded-bottom overflow-auto -overflow">
          <MenuPanel />
        </div>
      </div>
      <div class="flex-grow-1 d-flex flex-column align-items-stretch my-3">
        <div class="flex-grow-1 bg-white rounded mb-3 overflow-auto -overflow">
          <GameDisplayPanel />
        </div>
        <div class="bg-white rounded">
          <GameCommandPanel />
        </div>
      </div>
      <div class="d-none d-lg-flex flex-column align-items-stretch my-3 ms-3 -right-box">
        <div class="bg-white rounded-top border-bottom text-center p-2">
          チャットスペース
        </div>
        <div class="flex-grow-1 bg-white rounded-bottom">
          <ChatSpacePanel />
        </div>
      </div>
    </div>
  </div>
  <div class="offcanvas offcanvas-start -offcanvas-left" tabindex="-1" id="offcanvasLeft">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasLabel">ゲームメニュー</h5>
      <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
      <MenuPanel />
    </div>
  </div>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight">
    <div class="offcanvas-header">
      <h5 id="offcanvasRightLabel">チャットスペース</h5>
      <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
      <ChatSpacePanel />
    </div>
  </div>
  <MenuCommands />
</template>

<style scoped>
.-background {
  height: 100vh;
}

.-left-box {
  width: 200px;
}

.-right-box {
  width: 300px;
}

.-overflow {
  height: 0;
}

.-offcanvas-left {
  max-width: 240px;
}
</style>
