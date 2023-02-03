<script setup>
import Information from "./inside-screen-children/Information.vue"
import MenuPanel from "./inside-screen-children/MenuPanel.vue"
import GameDisplayPanel from "./inside-screen-children/GameDisplayPanel.vue"
import GameCommandPanel from "./inside-screen-children/GameCommandPanel.vue"
import ChatSpacePanel from "./inside-screen-children/ChatSpacePanel.vue"
</script>

<template>
  <div class="d-flex flex-column -background">
    <div class="d-flex d-lg-none align-items-center container-fluid bg-dark p-1">
      <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasLeft">
        <i class="bi bi-list fs-5"></i>
      </button>
      <div class="flex-grow-1">
        <Information on="bar" />
      </div>
      <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight">
        <i class="bi bi-chat-dots fs-5"></i>
      </button>
    </div>
    <div class="flex-grow-1 d-flex align-items-stretch container">
      <div class="d-none d-lg-flex flex-column align-items-stretch my-3 me-3 -left-box">
        <div class="bg-dark rounded mb-3">
          <Information on="box" />
        </div>
        <div class="flex-grow-1 bg-white rounded overflow-auto -overflow">
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
        <div class="flex-grow-1 bg-white rounded">
          <ChatSpacePanel header />
        </div>
      </div>
    </div>
  </div>
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasLeft">
    <div class="offcanvas-header py-2">
      <Information on="offcanvas-header" />
      <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
      <Information on="offcanvas-body" />
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
</style>
