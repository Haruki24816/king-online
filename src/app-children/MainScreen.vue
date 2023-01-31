<template>
  <div class="d-flex flex-column -base">
    <div class="d-flex d-lg-none align-items-center container-fluid bg-dark p-1">
      <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasLeft">
        <i class="bi bi-list fs-5"></i>
      </button>
      <div class="flex-grow-1 text-center">
        <div class="text-white -bar-room-name"><strong>部屋の名前</strong></div>
        <div class="text-white -bar-room-info">部屋の情報</div>
      </div>
      <button type="button" class="btn btn-dark" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight">
        <i class="bi bi-chat-dots fs-5"></i>
      </button>
    </div>
    <div class="d-flex align-items-stretch container flex-grow-1">
      <div class="d-none d-lg-flex flex-column align-items-stretch my-3 me-3 -left-box">
        <div class="bg-dark rounded mb-3">
          <br>
        </div>
        <div class="bg-white rounded flex-grow-1">
        </div>
      </div>
      <div class="d-flex flex-column align-items-stretch my-3 flex-grow-1">
        <div class="bg-white rounded flex-grow-1 mb-3">
        </div>
        <div class="bg-white rounded">
          <br>
        </div>
      </div>
      <div class="d-none d-lg-flex flex-column align-items-stretch my-3 ms-3 -right-box">
        <div class="bg-white rounded flex-grow-1 p-3">
        </div>
      </div>
    </div>
  </div>
  <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasLeft">
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="offcanvasLeftLabel"></h5>
      <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
    </div>
  </div>
  <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight">
    <div class="offcanvas-header">
      <h5 id="offcanvasRightLabel"></h5>
      <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
    </div>
  </div>
</template>

<style scoped>
.-base {
  height: 100vh;
}

.-left-box {
  width: 200px;
}

.-right-box {
  width: 300px;
}

.-bar-room-name {
  font-size: 16px;
}

.-bar-room-info {
  font-size: 12px;
}
</style>
